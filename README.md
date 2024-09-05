
# Paket Yakalama ve Okuma Script'i

Scapy kütüphanesini kullanarak ağ trafiğini yakalar, bu trafiği bir `.pcap` dosyasına kaydeder ve kaydedilen paketleri analiz eder. Script, ICMP paketlerini yakalarken kullanıcının belirttiği seçeneklere göre çalışır.

## Gereksinimler

- Python 3.x
- Scapy (`pip install scapy`)

## Nasıl Çalışır?

### 1. **Paket Yakalama (Sniff)**
   - `start_sniff()` fonksiyonu, ağ arayüzü (`eth0`) üzerinden 5 saniye boyunca paket yakalar.
   - Yakaladığı paketleri bir `.pcap` dosyasına (`Sum.pcap`) kaydeder.
   - ICMP paketleri algılandığında yakalama işlemi durur.



### 2. **Paket Okuma (Read)**
   - `start_read()` fonksiyonu, kaydedilen `Sum.pcap` dosyasındaki paketleri okur.
   - Her paketin IP katmanına bakar ve kaynak IP adreslerini bir listeye ekler.
   - Paketlerin IP katmanı yoksa, paketi ekrana yazdırır.
   


### 3. **Seçim**
   - Kullanıcıdan seçim yapması istenir:
     - `1`: Paketleri yakalar.
     - `2`: Kaydedilen paketleri okur.

## Kullanım

1. Script'i terminalden çalıştırın:

   ```bash
   sudo python3 NetworkSniffer.py
   ```

2. Paketleri yakalamak için `1`, kaydedilen paketleri okumak için `2` girin.

## Uyarı

Bu script, yalnızca ağ üzerinde izinli olduğunuz yerlerde kullanılmalıdır.

