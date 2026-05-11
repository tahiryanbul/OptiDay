from sqlalchemy import create_engine, text

db_user = 'root'      
db_password = ''      
db_name = 'planflow_db'
engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@localhost/{db_name}")

def yeni_kullanici_ekle(name, daily_standard_capacity):
    try:
        with engine.connect() as conn:
            query = text("""
                INSERT INTO Users (name, daily_standard_capacity)
                VALUES (:name, :cap)
            """)
            # İşlemi çalıştır ve sonucu bir değişkene ata
            result = conn.execute(query, {"name": name, "cap": daily_standard_capacity})
            conn.commit()
            
            # Veritabanının bu kullanıcıya otomatik atadığı AUTO_INCREMENT ID'yi yakala!
            yeni_id = result.lastrowid 
            
        print(f"👤 BAŞARILI: '{name}' eklendi! (Otomatik Atanan ID: {yeni_id})")
        return yeni_id # Bu ID'yi diğer fonksiyonlarda kullanmak için dışarı veriyoruz
        
    except Exception as e:
        print(f"❌ HATA: Kullanıcı eklenemedi: {e}")
        return None
    
def yeni_gorev_ekle(user_id, task_name, estimated_duration, mental_difficulty, urgency_level):
    """Belirli bir kullanıcıya yeni bir görev atar."""
    try:
        with engine.connect() as conn:
            query = text("""
                INSERT INTO Tasks (user_id, task_name, estimated_duration, mental_difficulty, urgency_level, status)
                VALUES (:uid, :tname, :dur, :diff, :urg, 'Pending')
            """)
            conn.execute(query, {
                "uid": user_id, "tname": task_name, 
                "dur": estimated_duration, "diff": mental_difficulty, "urg": urgency_level
            })
            conn.commit()
        print(f"✅ BAŞARILI: '{task_name}' görevi (Kullanıcı ID: {user_id}) eklendi!")
    except Exception as e:
        print(f"❌ HATA: Görev eklenemedi: {e}")

def gunluk_log_ekle(log_date, user_id, physical_activity_score, planned_total_duration=0):
    """Kullanıcının o günkü yorgunluk/aktivite durumunu sisteme girer."""
    try:
        with engine.connect() as conn:
            query = text("""
                INSERT INTO Daily_Logs (log_date, user_id, planned_total_duration, physical_activity_score)
                VALUES (:ldate, :uid, :pdur, :pscore)
            """)
            conn.execute(query, {
                "ldate": log_date, "uid": user_id, 
                "pdur": planned_total_duration, "pscore": physical_activity_score
            })
            conn.commit()
        print(f"📊 BAŞARILI: Kullanıcı ID {user_id} için {log_date} tarihli günlük log (Yorgunluk: {physical_activity_score}/10) eklendi!")
    except Exception as e:
        print(f"❌ HATA: Log eklenemedi: {e}")

# ==========================================
# TEST VE KULLANIM ALANI
# ==========================================
print("OptiDay Veritabanı Yönetim Sistemi\n" + "="*40)

# 1. Kullanıcıyı ekle ve veritabanının atadığı ID'yi yakala
zeynep_id = yeni_kullanici_ekle(name="Zeynep", daily_standard_capacity=7)

# Eğer kullanıcı başarıyla eklendiyse (ID boş değilse) görev ve log atamasını yap
if zeynep_id:
    yeni_gorev_ekle(
        user_id=zeynep_id, # Elle 4 yazmak yerine değişkeni kullandık!
        task_name="Makine Öğrenmesi Modeli Optimizasyonu", 
        estimated_duration=180, 
        mental_difficulty=5, 
        urgency_level=3
    )

    gunluk_log_ekle(
        log_date='2026-05-10', 
        user_id=zeynep_id, # Yine değişkeni kullandık
        physical_activity_score=7 
    )