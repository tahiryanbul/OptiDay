import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns

# Veritabanı Bağlantısı
db_user = 'root'      
db_password = ''      
db_name = 'planflow_db'
engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@localhost/{db_name}")

def gorsellestir_kapasite(kullanici_adi, standart, gercek, planlanan, onerilen):
    sns.set_theme(style="whitegrid")
    kategoriler = ['Standart Kapasite', 'Gerçek Kapasite (Yorgunluk Ayarlı)', 'İlk Planlanan Yük', 'OptiDay Önerisi']
    sureler = [standart, gercek, planlanan, onerilen]
    renkler = ['#4C72B0', '#55A868', '#C44E52', '#8172B3']
    
    plt.figure(figsize=(12, 6))
    ax = sns.barplot(x=kategoriler, y=sureler, hue=kategoriler, palette=renkler, legend=False)
    plt.title(f"OptiDay Analiz Raporu: {kullanici_adi}", fontsize=14, pad=15)
    plt.ylabel("Süre (Dakika)")
    
    for p in ax.patches:
        ax.annotate(f"{int(p.get_height())} dk", (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 9), textcoords='offset points')
    
    plt.tight_layout()
    plt.show()

def kullanici_kapasite_analizi(user_id, hedef_tarih, kullanici_adi):
    print(f"\n[ OptiDay {kullanici_adi} İçin Analiz Başlıyor - Tarih: {hedef_tarih} ]")
    print("=" * 65)
    
    query = f"""
        SELECT t.task_name, t.estimated_duration, t.mental_difficulty, t.urgency_level, u.daily_standard_capacity, d.physical_activity_score
        FROM Tasks t
        JOIN Users u ON t.user_id = u.id
        JOIN Daily_Logs d ON t.user_id = d.user_id
        WHERE t.user_id = {user_id} AND t.status = 'Pending' AND d.log_date = '{hedef_tarih}';
    """
    df = pd.read_sql(query, engine)
    if df.empty: return

    toplam_planlanan_sure = df['estimated_duration'].sum()
    standart_kapasite_dakika = df['daily_standard_capacity'].iloc[0] * 60
    fiziksel_yorgunluk = df['physical_activity_score'].iloc[0]

    if fiziksel_yorgunluk > 5:
        ceza_orani = (fiziksel_yorgunluk - 5) * 0.05
        gercek_kapasite_dakika = int(standart_kapasite_dakika * (1 - ceza_orani))
        df_sirali = df.sort_values(by=['urgency_level', 'mental_difficulty', 'estimated_duration'], ascending=[False, True, True])
        durum_mesaji = "Yüksek yorgunluk tespit edildi. Acil işleriniz korunarak, düşük eforlu görevler önceliklendirildi."
    else:
        gercek_kapasite_dakika = standart_kapasite_dakika
        df_sirali = df.sort_values(by=['urgency_level', 'mental_difficulty', 'estimated_duration'], ascending=[False, False, False])
        durum_mesaji = "Enerji seviyeniz ideal. En verimli olduğunuz bu sürede odaklanma gerektiren işler ilk sıraya alındı."

    print(f"Durum Analizi: {durum_mesaji}")
    print(f"Planlanan Yük: {toplam_planlanan_sure} dk | Mevcut Kapasite: {gercek_kapasite_dakika} dk\n")

    oneri_listesi = []
    harcanan_sure = 0

    if toplam_planlanan_sure > gercek_kapasite_dakika:
        print("💡 OptiDay Sürdürülebilir Gün Planı Önerisi:")
        for _, row in df_sirali.iterrows():
            if harcanan_sure + row['estimated_duration'] <= gercek_kapasite_dakika:
                oneri_listesi.append(row)
                harcanan_sure += row['estimated_duration']
        
        df_oneri = pd.DataFrame(oneri_listesi)
        print(df_oneri[['task_name', 'estimated_duration', 'urgency_level']].to_string(index=False))
        gorsellestir_kapasite(kullanici_adi, standart_kapasite_dakika, gercek_kapasite_dakika, toplam_planlanan_sure, harcanan_sure)
    else:
        print("✅ Mevcut planınız kapasite sınırları içinde, değişim önerilmiyor.")
        gorsellestir_kapasite(kullanici_adi, standart_kapasite_dakika, gercek_kapasite_dakika, toplam_planlanan_sure, toplam_planlanan_sure)

# Testler
kullanici_kapasite_analizi(1, '2026-05-09', 'Tahir')
kullanici_kapasite_analizi(2, '2026-05-09', 'Alex')
kullanici_kapasite_analizi(3, '2026-05-09', 'Sarah')