import subprocess
import platform

class NetworkMonitor:
    def __init__(self):
        self.ip_seznam = ["8.8.8.8", "1.1.1.1", "192.168.1.1", "1"]
        self.vysledky = {}

    def ping_ip(self, ip_adresa):
        parametr = '-n' if platform.system().lower() == 'windows' else '-c'
        prikaz = ['ping', parametr, '1', ip_adresa]
        
        try:
            odpoved = subprocess.run(prikaz, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return odpoved.returncode == 0
            
        except Exception as e:
            print(f"Chyba při pingu na {ip_adresa}: {e}")
            return False

    def spustit_kontrolu(self):
        """Projde všechny IP adresy v seznamu a zkontroluje je."""
        print("Začínám kontrolu sítě...\n" + "-"*30)
        
        for ip in self.ip_seznam:
            print(f"Testuji {ip}...", end=" ")
            
            if self.ping_ip(ip):
                print("[ OK ] - Zařízení žije")
                self.vysledky[ip] = "Online"
            else:
                print("[ CHYBA ] - Zařízení neodpovídá")
                self.vysledky[ip] = "Offline"
                
        print("-"*30 + "\nKontrola dokončena!")

# main
if __name__ == "__main__":
    monitor = NetworkMonitor()
    monitor.spustit_kontrolu()