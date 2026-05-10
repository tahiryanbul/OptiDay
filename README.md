
# OptiDay: AI Destekli Günlük Kapasite Optimizasyon Sistemi

## 🎯 Seçilen Problem
**Problem 5 - Bir Güne Fazla Görev Sığdırmaya Çalışma:** Kullanıcıların gerçekçi olmayan, fiziksel ve zihinsel sınırları zorlayan sürdürülemez planlar oluşturması ve bunun sonucunda oluşan motivasyon kaybı ve tükenmişlik.

## 💡 Proje Özeti
**OptiDay**, sıradan bir yapılacaklar listesinin ötesine geçerek kullanıcının o günkü **fiziksel yorgunluğunu** ve görevlerin **zihinsel zorluk derecesini** analiz eder. Yapay zeka destekli altyapısı sayesinde, kapasite aşımı durumunda kullanıcıyı uyarmakla kalmaz; aciliyet, efor ve enerji seviyesine göre optimize edilmiş, sürdürülebilir bir alternatif plan önerir.

## 🛠️ Kullanılan Teknolojiler
* **Dil:** Python 
* **Veri Analizi:** Pandas, NumPy
* **Veritabanı:** MySQL (SQLAlchemy, PyMySQL)
* **Görselleştirme:** Seaborn, Matplotlib

## 🚀 Kurulum ve Çalıştırma

**1. Repoyu Klonlayın:**
```bash
git clone https://github.com/tahiryanbul/OptiDay.git
cd OptiDay

2. Sanal Ortamı Kurun ve Aktifleştirin:

**2. Sanal Ortamı Kurun ve Aktifleştirin:**

```bash
# Windows için:
python -m venv venv
.\venv\Scripts\activate

# Mac/Linux için:
python3 -m venv venv
source venv/bin/activate

3. Gerekli Paketleri Yükleyin:

pip install -r requirements.txt

4. Veritabanını Hazırlayın:

MySQL üzerinde planflow_db adında bir veritabanı oluşturun.

Proje dizinindeki database_setup.sql içeriğini çalıştırarak tabloları ve mock verileri yükleyin.


5. Sistemi Çalıştırma (Kullanım)
OptiDay mimarisi iki ana modülden oluşmaktadır:

Modül 1: Dinamik Veri Yönetimi (Backend API Simülasyonu)
Projeye SQL arayüzü kullanmadan, doğrudan Python üzerinden dinamik olarak yeni kullanıcı, görev ve günlük log ekleyebilirsiniz. Sistem, AUTO_INCREMENT ile oluşturulan yeni kullanıcı ID'lerini otomatik yakalayarak ilişkisel (Foreign Key) veri bütünlüğünü sağlar.

Sisteme yeni bir kullanıcı profili ve görevler eklemek için test dosyasını çalıştırın:

Bash
python veri_ekle.py
Modül 2: Yapay Zeka Kapasite Analizi ve Görselleştirme
Sistemdeki kullanıcıların o günkü yorgunluk skorlarını ve görev yüklerini analiz etmek için ana motoru çalıştırın.

Bash
python analyzer.py
Bu komut, her kullanıcı için terminalde detaylı bir durum raporu oluşturur ve Seaborn kütüphanesi ile kapasite aşımlarını/optimizasyonları gösteren interaktif grafikler (Dashboard) çizer.