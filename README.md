
# OptiDay: AI Destekli Günlük Kapasite Optimizasyon Sistemi

## 🎯 Seçilen Problem
**Problem 5 - Bir Güne Fazla Görev Sığdırmaya Çalışma:** Kullanıcıların gerçekçi olmayan, fiziksel ve zihinsel sınırları zorlayan sürdürülemez planlar oluşturması ve bunun sonucunda oluşan motivasyon kaybı ve tükenmişlik.

## 💡 Proje Özeti
**OptiDay**, sıradan bir yapılacaklar listesinin ötesine geçerek kullanıcının o günkü **fiziksel yorgunluğunu** ve görevlerin **zihinsel zorluk derecesini** analiz eder. Yapay zeka destekli altyapısı sayesinde, kapasite aşımı durumunda kullanıcıyı uyarmakla kalmaz; aciliyet, efor ve enerji seviyesine göre optimize edilmiş, sürdürülebilir bir alternatif plan önerir.

## 🛠️ Kullanılan Teknolojiler
* **Dil:** Python 3.x
* **Veri Analizi:** Pandas, NumPy
* **Veritabanı:** MySQL (SQLAlchemy, PyMySQL)
* **Görselleştirme:** Seaborn, Matplotlib

## 🚀 Kurulum ve Çalıştırma

**1. Repoyu Klonlayın:**
```bash
git clone https://github.com/tahiryanbul/OptiDay.git
cd OptiDay

**2. Sanal Ortamı Kurun ve Aktifleştirin:**

python -m venv venv
.\venv\Scripts\activate  # Windows için

python3 -m venv venv
source venv/bin/activate  # Mac için

**3. Gerekli Paketleri Yükleyin:**

pip install -r requirements.txt

**4. Veritabanını Hazırlayın:**

MySQL üzerinde planflow_db adında bir veritabanı oluşturun.

Proje dizinindeki database_setup.sql içeriğini çalıştırarak tabloları ve mock verileri yükleyin.

**5. Yapılandırma:**

analyzer.py içindeki db_user ve db_password alanlarını kendi yerel MySQL bilgilerinizle güncelleyin.

6. Sistemi Başlatın:

python analyzer.py

