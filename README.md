SC4RLEY - High-Speed TLD Grabber 🚀

SC4RLEY is an ultra-fast, multi-threaded TLD grabber designed to efficiently scan and retrieve top-level domains. Built for speed and precision, it ensures you get the most relevant domain data in record time!

⚡ Features

Multi-threaded Performance - Blazing-fast domain scanning.

Highly Optimized - Minimal resource consumption.

Customizable Queries - Search specific TLDs.

Real-time Output - Instant results display.

Lightweight & Portable - No unnecessary dependencies.

Fake-Headers Integration - Mimics real browser headers for better accuracy.

🛠️ Installation

# Clone the repository
git clone https://github.com/yourusername/SC4RLEY.git

# Navigate into the project folder
cd SC4RLEY

# Install dependencies
pip install -r requirements.txt

🚀 Usage

python sc4rley.py -tld com

Arguments:

-tld : Target TLD to scan (required)

🏆 Why SC4RLEY?

Speed: Multi-threading makes it one of the fastest TLD grabbers.

Simplicity: Easy-to-use CLI with intuitive commands.

Accuracy: Fetches only valid TLDs without unnecessary data.

Fake-Headers Support: Avoids detection by imitating real browser headers.

📦 Fake-Headers Integration

SC4RLEY utilizes fake_useragent to generate dynamic and realistic HTTP headers, enhancing reliability when querying domains.

Installing Fake-Headers

pip install fake-useragent

Example Usage

SC4RLEY automatically integrates fake_useragent, so no additional configuration is required.

from fake_useragent import UserAgent
headers = {'User-Agent': UserAgent().random}
print(headers)

🛡️ Disclaimer

This tool is intended for educational and research purposes only. The author is not responsible for any misuse.

🇹🇷 SC4RLEY - Yüksek Hızlı TLD Grabber 🚀

SC4RLEY, üst düzey alan adlarını (TLD) taramak ve almak için tasarlanmış, ultra hızlı, çok iş parçacıklı (multi-threaded) bir grabber aracıdır. Hız ve doğruluk için optimize edilmiştir!

⚡ Özellikler

Çoklu İş Parçacığı (Multi-threading) - Son derece hızlı tarama.

Yüksek Performans - Minimum kaynak kullanımı.

Özelleştirilebilir Aramalar - Belirli TLD'leri tarama imkanı.

Gerçek Zamanlı Çıktı - Anında sonuç görüntüleme.

Hafif ve Taşınabilir - Gereksiz bağımlılıklar içermez.

Fake-Headers Entegrasyonu - Gerçek tarayıcı başlıklarını taklit eder.

🛠️ Kurulum

# Depoyu klonlayın
git clone https://github.com/yourusername/SC4RLEY.git

# Proje klasörüne girin
cd SC4RLEY

# Bağımlılıkları yükleyin
pip install -r requirements.txt

🚀 Kullanım

python sc4rley.py -tld com

Parametreler:

-tld : Hedef üst düzey alan adı (zorunlu)

🏆 Neden SC4RLEY?

Hızlı: Multi-threading ile en hızlı TLD grabber'lardan biri.

Kullanıcı Dostu: Basit ve anlaşılır komut satırı arayüzü.

Kesinlik: Gereksiz veriler olmadan yalnızca geçerli TLD'leri alır.

Fake-Headers Desteği: Gerçek tarayıcı başlıkları kullanarak tespit edilmeden sorgulama yapar.

📦 Fake-Headers Entegrasyonu

SC4RLEY, fake_useragent kullanarak gerçekçi HTTP başlıkları oluşturur ve sorgulama güvenilirliğini artırır.

Fake-Headers Kurulumu

pip install fake-useragent

Kullanım Örneği

SC4RLEY, fake_useragent entegrasyonunu otomatik olarak yapar, ekstra yapılandırmaya gerek yoktur.

from fake_useragent import UserAgent
headers = {'User-Agent': UserAgent().random}
print(headers)

🛡️ Yasal Uyarı

Bu araç yalnızca eğitim ve araştırma amaçlıdır. Yanlış kullanım tamamen kullanıcının sorumluluğundadır.
