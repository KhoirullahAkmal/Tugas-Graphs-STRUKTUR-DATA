class Peta:
    def _init_(self):
        self.cityList = {}
    
    def printPeta(self):
        for kota in self.cityList:
            print(kota, ":",self.cityList[kota])
        
    def tambahkanKota(self,kota):
        if kota not in self.cityList:
            self.cityList[kota] = []
            return True
        return False
    
    def hapusKota(self,kotaDihapus):
        #cek apakah kota yang ingin dihapus ada di list
        if kotaDihapus in self.cityList:
        #iterasi setiap kotalain untuk hapus kotadihapus
            for kotalain in self.cityList:
                #cek apakah kota yang ingin dihapus ada jalannya ke kotalain
                if kotaDihapus in self.cityList[kotalain]:
                    self.cityList[kotalain].remove(kotaDihapus)
            del self.cityList[kotaDihapus]
            return True
        return False

     def tambahkanJalan(self,kota1,kota2):
        if kota1 in self.cityList and kota2 in self.cityList:
            #masukkan kota 1 di list kota2
            self.cityList[kota2].append(kota1)
            #masukkan kota 2 di list kota1
            self.cityList[kota1].append(kota2)
            return True
        return False
    
    def hapusJalan(self,kota1,kota2):
        if kota1 in self.cityList and kota2 in self.cityList:
            #hapus kota 1 di list kota2
            self.cityList[kota2].remove(kota1)
            #hapus kota 2 di list kota1
            self.cityList[kota1].remove(kota2)
            return True
        return False

petaArab = Peta()
petaArab.tambahkanKota("Yanbu")
petaArab.tambahkanKota("Madinah")
petaArab.tambahkanKota("Kota Badar")
petaArab.tambahkanKota("Al Henakiyah")
petaArab.tambahkanKota("Rabigh")
petaArab.tambahkanKota("Mahd adh Dhahab")
petaArab.tambahkanKota("Jeddah")
petaArab.tambahkanKota("Ta'if")
petaArab.tambahkanKota("Turbah")
petaArab.tambahkanKota("Ranyah")
petaArab.tambahkanKota("Al Khurma")
petaArab.tambahkanKota("Dariyah")
petaArab.tambahkanKota("Ar Rass")
petaArab.tambahkanKota("Al Quwaiiyah")
petaArab.tambahkanKota("Layla")
petaArab.tambahkanJalan("Yanbu","Madinah")
petaArab.tambahkanJalan("Yanbu","Kota Badar")
petaArab.tambahkanJalan("Yanbu","Rabigh")
petaArab.tambahkanJalan("Madinah","Kota Badar")
petaArab.tambahkanJalan("Madinah","Al Henakiyah")
petaArab.tambahkanJalan("Madinah","Mahd adh Dhahab")
petaArab.tambahkanJalan("Kota Badar","Rabigh")
petaArab.tambahkanJalan("Kota Badar","Ta'if")
petaArab.tambahkanJalan("Al Henakiyah","Al Kurma")
petaArab.tambahkanJalan("Al Henakiyah","Dariyah")
petaArab.tambahkanJalan("Al Henakiyah","Ar Rass")
petaArab.tambahkanJalan("Rabigh","Mahd adh Dhahab")
petaArab.tambahkanJalan("Rabigh","Jeddah")
petaArab.tambahkanJalan("Mahd adh Dhahab","Ta'if")
petaArab.tambahkanJalan("Mahd adh Dhahab","Al Kurma")
petaArab.tambahkanJalan("Mahd adh Dhahab","Dariyah")
petaArab.tambahkanJalan("Mahd adh Dhahab","Dariyah")
petaArab.tambahkanJalan("Jeddah","Ta'if")
petaArab.tambahkanJalan("Jeddah","Mahd adh Dhahab")
petaArab.tambahkanJalan("Ta'if","Turbah")
petaArab.tambahkanJalan("Turbah","Al Khurma")
petaArab.tambahkanJalan("Turbah","Ranyah")
petaArab.tambahkanJalan("Ranyah","Al Khurma")
petaArab.tambahkanJalan("Ranyah","Al Quwaiiyah")
petaArab.tambahkanJalan("Ranyah","Layla")
petaArab.tambahkanJalan("Al Khurma","Dariyah")
petaArab.tambahkanJalan("Al Khurma","Al Quwaiiyah")
petaArab.tambahkanJalan("Dariyah","Ar Rass")
petaArab.tambahkanJalan("Dariyah","Al Quwaiiyah")
petaArab.tambahkanJalan("Dariyah","Layla")
petaArab.tambahkanJalan("Al Quwaiiyah","Ar Rass")
petaArab.tambahkanJalan("Al Quwaiiyah","Layla")
petaArab.printPeta()

    
