# Github-Project-Recommender
This code creates a GitHub project recommendation interface using Tkinter. Users can upload GitHub user, project, and star data. Based on selected users or projects, the code provides recommendations using different similarity algorithms. 



# English
# GitHub Project Recommender

This is a Python application that recommends GitHub projects and users based on star data. It uses collaborative filtering techniques to provide personalized recommendations.

## Features

- Upload user data: Allows you to upload a text file containing user data, including user IDs, usernames, and links.
- Upload repository data: Lets you upload a text file containing repository data, including user IDs, usernames, repository URLs, and programming languages.
- Upload star data: Enables you to upload a text file containing star data, which represents the user-star interactions.
- Recommend repositories: Recommends repositories based on the selected user and programming language.
- Recommend GitHub users: Recommends GitHub users based on the selected repository and programming language.
- Filter by programming language: Filters recommendations based on the selected programming language.
- Distance algorithm: Allows you to choose between Pearson correlation coefficient and Euclidean distance as the distance algorithm for similarity calculation.
- Number of recommendations: Specifies the number of recommendations to display.

## How to Use

1. Clone the repository or download the files.
2. Install the required dependencies by running the command `pip install -r requirements.txt`.
3. Run the `main.py` file to start the application.
4. Use the "Upload User Data" button to upload a text file containing user data.
5. Use the "Upload Repository Data" button to upload a text file containing repository data.
6. Use the "Upload Star Data" button to upload a text file containing star data.
7. Select a user from the left panel to recommend repositories or GitHub users.
8. Select a programming language to filter the recommendations (optional).
9. Choose a distance algorithm for similarity calculation.
10. Specify the number of recommendations to display (optional).
11. Click the corresponding button ("Recommend Repository" or "Recommend GitHub User") to get the recommendations.
12. The recommendations will be displayed in the right panel.

Feel free to customize and enhance the application according to your needs.

## Dependencies

- Python 3.x
- tkinter
- ttk
- filedialog
- recommendations


# Türkçe
# Github Project Recommender

Github Project Recommender, kullanıcıların ve projelerin GitHub üzerindeki verilerini kullanarak öneriler sunan bir uygulamadır.

## Özellikler

- Kullanıcı verilerini yükleyebilme
- Proje verilerini yükleyebilme
- Yıldız verilerini yükleyebilme
- Kullanıcılara ve projelere göre öneriler alabilme
- Programlama diline ve benzerlik algoritmasına göre filtreleme seçeneği

## Kullanım

1. **Upload User Data** düğmesine tıklayarak kullanıcı verilerini yükleyin. Veri dosyası bir metin dosyası (.txt) formatında olmalıdır ve her satırda bir kullanıcı bilgisi bulunmalıdır. Kullanıcı bilgileri virgülle ayrılmış şekilde sırasıyla kullanıcı ID'si, kullanıcı adı ve link içermelidir.

2. **Upload Repository Data** düğmesine tıklayarak proje verilerini yükleyin. Veri dosyası bir metin dosyası (.txt) formatında olmalıdır ve her satırda bir proje bilgisi bulunmalıdır. Proje bilgileri virgülle ayrılmış şekilde sırasıyla kullanıcı ID'si, kullanıcı adı, URL ve programlama dili içermelidir.

3. **Upload Star Data** düğmesine tıklayarak yıldız verilerini yükleyin. Veri dosyası bir metin dosyası (.txt) formatında olmalıdır. Dosyanın her satırı bir kullanıcının yıldız verilerini içermeli ve kullanıcı ID'si ile yıldız değerleri tab ile ayrılmış şekilde belirtilmelidir.

4. **Recommend Repository** düğmesine tıklayarak seçili kullanıcı için proje önerilerini alın. Öneriler, belirli bir programlama diline ve benzerlik algoritmasına göre filtrelenmiş olacaktır. İstenirse öneri sayısı da belirtilebilir.

5. **Recommend Github User** düğmesine tıklayarak seçili proje için kullanıcı önerilerini alın. Öneriler, belirli bir programlama diline ve benzerlik algoritmasına göre filtrelenmiş olacaktır. İstenirse öneri sayısı da belirtilebilir.

## Nasıl Kullanılır

1. Depoyu klonlayın veya dosyaları indirin.
2. Gerekli bağımlılıkları yüklemek için `pip install -r requirements.txt` komutunu çalıştırın.
3. Uygulamayı başlatmak için `main.py` dosyasını çalıştırın.
4. Kullanıcı verilerini içeren bir metin dosyasını yüklemek için "Kullanıcı Verilerini Yükle" düğmesini kullanın.
5. Depo verilerini içeren bir metin dosyasını yüklemek için "Depo Verilerini Yükle" düğmesini kullanın.
6. Yıldız verilerini içeren bir metin dosyasını yüklemek için "Yıldız Verilerini Yükle" düğmesini kullanın.
7. Sağ paneldeki kullanıcılardan birini seçerek depoları veya GitHub kullanıcılarını önerin.
8. Önerileri filtrelemek için bir programlama dilini seçin (isteğe bağlı).
9. Benzerlik hesaplaması için bir uzaklık algoritması seçin.
10. Görüntülenecek öneri sayısını belirtin (isteğe bağlı).
11. Önerileri almak için ilgili düğmeye ("Depo Öner" veya "GitHub Kullanıcısı Öner") tıklayın.
12. Öneriler sağ panelde görüntülenecektir.
