from tkinter import *
from tkinter import ttk, filedialog

from recommendations import *


class GithubProjectRecommender(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.repo_data = []
        self.user_data = []
        self.star_data = {}
        self.id = ""
        self.CheckVar1 = IntVar()
        self.CheckVar2 = IntVar()
        self.init_UI(parent)

    def upload_user_data(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

        if file_path:
            try:
                # Delete existing data from Treeview
                self.repo_view.delete(*self.repo_view.get_children())

                # Delete existing data
                self.user_data.clear()

                with open(file_path, "r") as file:
                    for line in file:
                        line = line.strip()
                        if line:  # Boş satırları atlayın
                            parts = line.split(",")
                            if len(parts) >= 3:
                                user_id = parts[0].strip()
                                username = parts[1].strip()
                                link = parts[2].strip()
                                self.user_data.append((user_id, username, link))

                    user_data = sorted(self.user_data, key=lambda x: x[1])  # Kullanıcı adına göre sıralama
                    print(user_data)
                    for user_id, username, _ in user_data:
                        self.repo_view.insert("", "end", values=(username, user_id))

            except FileNotFoundError:
                print("Dosya bulunamadı.")

    def upload_data_to_combobox(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

        if file_path:
            try:
                self.repo_data.clear()

                with open(file_path, "r") as file:
                    for line in file:
                        line = line.strip()
                        if line:  # Boş satırları atlayın
                            parts = line.split(",")
                            if len(parts) >= 4:
                                user_id = parts[0].strip()
                                username = parts[1].strip()
                                url = parts[2].strip()
                                language = parts[3].strip()
                                self.repo_data.append((user_id, username, url, language))

                    repo_data = sorted(self.repo_data, key=lambda x: x[1])  # Kullanıcı adına göre sıralama
                    print(repo_data)

                    data_lang = [data[3] for data in repo_data if len(data) >= 4]
                    unique_data = list(set(data_lang))  # Tekrarlananları kaldır

                    unique_data.sort()  # Alfabetik olarak sırala
                    unique_data.insert(0, 'None')  # 'none' değerini ilk sıraya ekle

                    self.combobox['values'] = unique_data
                    self.combobox.current(0)  # İlk değeri seçili olarak ayarla

            except FileNotFoundError:
                print("Dosya bulunamadı.")

    def upload_star_data(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

        if file_path:
            try:
                self.star_data.clear()

                with open(file_path, "r") as file:

                    # Dosyayı satır satır okuyun
                    for line in file:
                        line = line.strip()  # Satırın başındaki ve sonundaki boşlukları kaldırın
                        if line:  # Boş satırları atlayın
                            # Satırı tab ile ayırarak verileri alın
                            parts = line.split("\t")
                            if len(parts) >= 2:
                                user_id = int(parts[0].strip())
                                star_values = [int(x) for x in parts[1].split(",")]
                                self.star_data[user_id] = {}  # Kullanıcıya ait boş bir sözlük oluşturun
                                for value in star_values:
                                    self.star_data[user_id][value] = 5.0  # Her değeri 5.0 olarak ayarlayın
                print(self.star_data)
                # Elde edilen star_data sözlüğünü kullanmak için istediğiniz işlemleri yapabilirsiniz
                # Örneğin, bu sözlüğü bir sınıf özelliği olarak kullanabilir veya başka bir fonksiyona aktarabilirsiniz

            except FileNotFoundError:
                print("Dosya bulunamadı.")

    def show_selected_id(self, event):
        selected_item = self.repo_view.selection()  # Seçili olan öğeyi al
        if selected_item:  # Seçili bir öğe varsa devam et
            values = self.repo_view.item(selected_item)["values"]  # Öğenin değerlerini al
            username = values[0]  # Kullanıcı adını al
            self.id = values[1]  # Id'yi al
            print(f"Seçili kullanıcının ID'si: {self.id}")

    def repo_recommend(self):
        if self.id is None:
            print("Please select a user from the repository view.")
            return

        number_of_recommendations = self.input.get()

        if self.CheckVar1.get() == 1:  # Person checkbox'ı seçili ise
            similarity_function = sim_pearson
        elif self.CheckVar2.get() == 1:  # Euclidean checkbox'ı seçili ise
            similarity_function = sim_distance
        else:
            print("Please select a distance algorithm.")
            return

        if number_of_recommendations.strip() == "":
            recommendations = getRecommendations(self.star_data, self.id, similarity=similarity_function)
        else:
            recommendations = getRecommendations(self.star_data, self.id, similarity=similarity_function)

        selected_language = self.combobox.get()  # Combobox'tan seçilen dil değerini al

        filtered_recommendations = []
        for score, item in recommendations:
            for data in self.repo_data:
                if data[0] == str(item):
                    if selected_language == 'None' or data[3] == selected_language:
                        filtered_recommendations.append((score, item))
                        break

        if number_of_recommendations.strip() != "":
            filtered_recommendations = filtered_recommendations[:int(number_of_recommendations)]

        self.recom_view.delete(*self.recom_view.get_children())  # Mevcut önerileri temizle

        for score, item in filtered_recommendations:
            for data in self.repo_data:
                if data[0] == str(item):
                    repo_name = data[1]
                    url = data[2]
                    self.recom_view.insert("", "end", values=(repo_name, url, round(score, 2)))
                    break

    def recommend_users(self):
        if self.id is None:
            print("Please select a user from the repository view.")
            return

        number_of_recommendations = self.input.get()

        if self.CheckVar1.get() == 1:  # Person checkbox'ı seçili ise
            similarity_function = sim_pearson
        elif self.CheckVar2.get() == 1:  # Euclidean checkbox'ı seçili ise
            similarity_function = sim_distance
        else:
            print("Please select a distance algorithm.")
            return

        if number_of_recommendations.strip() == "":
            recommendations = topMatches(self.star_data, self.id, similarity=similarity_function)
        else:
            recommendations = topMatches(self.star_data, self.id, similarity=similarity_function)

        selected_language = self.combobox.get()  # Combobox'tan seçilen dil değerini al

        filtered_recommendations = []
        for score, item in recommendations:
            for data in self.user_data:
                if data[0] == str(item):
                    if selected_language == 'None' or data[3] == selected_language:
                        filtered_recommendations.append((score, item))
                        break

        if number_of_recommendations.strip() != "":
            filtered_recommendations = filtered_recommendations[:int(number_of_recommendations)]

        self.recom_view.delete(*self.recom_view.get_children())  # Mevcut önerileri temizle

        for score, item in filtered_recommendations:
            for data in self.user_data:
                if data[0] == str(item):
                    repo_name = data[1]
                    url = data[2]
                    self.recom_view.insert("", "end", values=(repo_name, url, round(score, 2)))
                    break

    def init_UI(self, parent) -> None:

        # Uygulamanın adı
        self.baslik = Label(text="Github Project Recommender", bg="orange", font=('Arial', 24), width=61, fg="white")
        self.baslik.grid(row=0, column=0, columnspan=5)
        # button
        self.user_btn = Button(text="Upload User Data", height=2, command=self.upload_user_data)
        self.repo_btn = Button(text="Upload Repository Data", height=2, command=self.upload_data_to_combobox)
        self.star_btn = Button(text="Upload Star Data", height=2, command=self.upload_star_data)

        self.user_btn.grid(row=1, column=0, pady=20)
        self.repo_btn.grid(row=1, column=2, pady=20)
        self.star_btn.grid(row=1, column=4, pady=20)
        # textarea1
        self.recommen = Label(text="Recommendations")
        self.recommen.grid(row=2, column=4)

        self.repo_btn = Button(text="Recommend Repository", height=2, command=self.repo_recommend)
        self.repo_btn.grid(row=2, column=1, sticky=S, rowspan=2, pady=45)
        # textarea2
        self.recommen_repo = Label(text="Recommend Repository For")
        self.recommen_repo.grid(row=3, column=0, sticky=N)

        # textarea3

        self.text_filter = Label(text="Filter by programming language:")
        self.text_filter.grid(row=4, column=0)

        # textarea4
        self.text_algorithm = Label(text="Distance algorithm:")
        self.text_algorithm.grid(row=5, column=0)
        # button1
        self.git_btn = Button(text="Recommend Github User", height=2, command=self.recommend_users)
        self.git_btn.grid(row=3, column=1, sticky=S)

        # Treeveiw-left
        self.repo_view = ttk.Treeview(columns=("Username", "Id"), show="headings")
        self.repo_view.column("Username", width=120)
        self.repo_view.column("Id", width=60)
        self.repo_view.heading('Username', text='Username')
        self.repo_view.heading('Id', text='Id')
        self.repo_view.grid(row=3, column=0, sticky=S)
        self.repo_view.bind("<<TreeviewSelect>>", self.show_selected_id)

        # Treeveiw-right
        self.recom_view = ttk.Treeview(columns=("Name", "Url", "Score"), show="headings", height=25)
        self.recom_view.column("Name", width=90)
        self.recom_view.column("Url", width=210)
        self.recom_view.column("Score", width=80)
        self.recom_view.heading("Name", text="Name")
        self.recom_view.heading("Url", text="Url")
        self.recom_view.heading("Score", text="Score")
        self.recom_view.grid(row=3, column=4, rowspan=6)

        # Combobox
        self.combobox = ttk.Combobox(state='readonly')
        self.combobox.grid(row=4, column=0, sticky=S)

        def toggle_checkbox1():
            if self.CheckVar1.get() == 1:
                self.CheckVar2.set(0)

        def toggle_checkbox2():
            if self.CheckVar2.get() == 1:
                self.CheckVar1.set(0)

        chk_box_1 = Checkbutton(text="Pearson", variable=self.CheckVar1, onvalue=1, offvalue=0,
                                command=toggle_checkbox1)
        chk_box_1.grid(row=5, column=0, sticky=S)

        chk_box_2 = Checkbutton(text="Euclidean", variable=self.CheckVar2, onvalue=1, offvalue=0,
                                command=toggle_checkbox2)
        chk_box_2.grid(row=6, column=0, sticky=N)
        # last_are
        self.input = Entry(width=3, )
        self.input.grid(row=7, column=0, sticky=NE, padx=50)

        self.number_recom = Label(text="Number of Recommendetaions:", )
        self.number_recom.grid(row=7, column=0, sticky=NW)


def main():
    root = Tk()  # Pencere oluşturma
    root.title("Github Project Recommender")
    root.resizable(False, False)

    window_width = 1150
    window_height = 700
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    app = GithubProjectRecommender(root)
    root.mainloop()


main()
