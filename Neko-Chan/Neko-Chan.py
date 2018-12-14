import sys
import httplib
import socket

class bcolors: #Ini Warna
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'

class adminfinder():
    print ""
    print bcolors.HEADER + "\t##################### Created PhobiaXploit  " + bcolors.ENDC
    print bcolors.HEADER + "\t#+-+-+-+-+-+-+-+-+-+# Author ./Tsuki " + bcolors.ENDC
    print bcolors.HEADER + "\t# N e k o - C h a n # Thanks To:Ms Takyun-Mr Result-Mr.Cay-Dominic404 " + bcolors.ENDC
    print bcolors.HEADER + "\t#+-+-+-+-+-+-+-+-+-+# g03nj4t-Mr.Xyno-W4h7u_RASTAFARA-Mr.G0L34H " + bcolors.ENDC
    print bcolors.HEADER + "\t##################### Tu4n_B4J4nG-3RL4ND1" + bcolors.ENDC
    print ""

    def __init__(self):
        self.admin_locate()

    def admin_locate(self):
        try:
            try:
                site = raw_input(bcolors.BLUE + "Masukan URL: " + bcolors.ENDC)
                site = site.replace("http://", "")
                print bcolors.YELLOW + "\n\t[*] Mengecek../.. website " +  site + bcolors.ENDC
                conn = httplib.HTTPConnection(site)
                conn.connect()  # Menghubungkan website
                print bcolors.GREEN + "\t[+] Koneksi Ditetapkan,Ini Sedang Online.\n" + bcolors.ENDC
            except (httplib.HTTPResponse, socket.error) as Exit:
                print bcolors.RED + "\t[!] Tidak Dapat Terhubung Ke Website, Jika Error Jangan Gunakan Slash(/).\n" + bcolors.ENDC
                sys.exit()

            print bcolors.YELLOW + "\t[*] Mengecek: " + site + bcolors.ENDC + "\n"


            # Ini Wibu
            wordfile = open("wibu.txt", "r")
            wibu = wordfile.readlines()
            wordfile.close()

            for word in wibu:
                admin = word.strip("\n")
                admin = "/" + admin
                target = site + admin
                print bcolors.YELLOW + "[*] mengecek: " + target + bcolors.ENDC
                connection = httplib.HTTPConnection(site)
                connection.request("GET", admin)
                response = connection.getresponse()


                # Respon Status!....
                if response.status == 200:
                    print bcolors.GREEN + "\n\n\t+------------------------------------------------------+" + bcolors.ENDC
                    print "%s %s" % (bcolors.GREEN + "\t[*] Neko Ketemu.... >> " + bcolors.ENDC, bcolors.GREEN + target + bcolors.ENDC)
                    print bcolors.RED + "\t[!]200 Ok \n" + bcolors.ENDC
                    print bcolors.GREEN + "\t+------------------------------------------------------+\n" + bcolors.ENDC
                    raw_input(bcolors.YELLOW + "[*] Tekan Enter Untuk Melanjutkan../...\n" + bcolors.ENDC)
                elif response.status == 302:
                    print bcolors.RED + "[!] 302 Object moved temporarily.\n" + bcolors.ENDC
                elif response.status == 404:
                    print bcolors.RED + "[!] 404 Not Found.\n" + bcolors.ENDC
                elif response.status == 410:
                    print bcolors.RED + "[!] 410 Object removed permanently.\n" + bcolors.ENDC
                else:
                    print "%s %s %s %s" % (bcolors.RED + "Respon Tidak Diketahui: " + bcolors.ENDC, bcolors.RED + response.status + bcolors.ENDC, "\n", bcolors.RED + host + bcolors.ENDC)
                connection.close() # Koneksi Ditutup

        except (httplib.HTTPResponse, socket.error):
            print bcolors.RED + "\n\t[!] Sesi Dibatalkan../..." + bcolors.ENDC
            print bcolors.RED + "\t[!] Periksa Koneksi Internet" + bcolors.ENDC
        except (KeyboardInterrupt, SystemExit):
            print bcolors.RED + "\t[!] Sesi Dibatalkan../..." + bcolors.ENDC

if __name__ == "__main__":
    adminfinder()
