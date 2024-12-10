class Reminder:
    def _init_(self, title, description, date):
        self.title = title
        self.description = description
        self.date = date

    def _str_(self):
        return f"Title: {self.title}\nDescription: {self.description}\nDate: {self.date}"


class ReminderManager:
    def _init_(self):
        self.reminders = []

    def add_reminder(self, reminder):
        self.reminders.append(reminder)
        print("Reminder added successfully.")

    def edit_reminder(self, index, title=None, description=None, date=None):
        if 0 <= index < len(self.reminders):
            if title:
                self.reminders[index].title = title
            if description:
                self.reminders[index].description = description
            if date:
                self.reminders[index].date = date
            print("Reminder updated successfully.")
        else:
            print("Invalid index.")

    def delete_reminder(self, index):
        if 0 <= index < len(self.reminders):
            del self.reminders[index]
            print("Reminder deleted successfully.")
        else:
            print("Invalid index.")

    def display_reminders(self):
        if not self.reminders:
            print("No reminders found.")
        else:
            for i, reminder in enumerate(self.reminders):
                print(f"\nReminder {i + 1}:\n{reminder}")


# Contoh penggunaan
if __name__ == "__main__":
    manager = ReminderManager()

    while True:
        print("\nAplikasi Reminder Sederhana")
        print("1. Tambah Reminder")
        print("2. Edit Reminder")
        print("3. Hapus Reminder")
        print("4. Tampilkan Reminder")
        print("5. Keluar")

        choice = input("Pilih opsi (1-5): ")
        if choice == "1":
            title = input("Masukkan judul: ")
            description = input("Masukkan deskripsi: ")
            date = input("Masukkan tanggal (YYYY-MM-DD): ")
            reminder = Reminder(title, description, date)
            manager.add_reminder(reminder)
        elif choice == "2":
            index = int(input("Masukkan nomor reminder yang ingin diedit: ")) - 1
            title = input("Masukkan judul baru (kosongkan jika tidak diubah): ")
            description = input("Masukkan deskripsi baru (kosongkan jika tidak diubah): ")
            date = input("Masukkan tanggal baru (kosongkan jika tidak diubah): ")
            manager.edit_reminder(index, title or None, description or None, date or None)
        elif choice == "3":
            index = int(input("Masukkan nomor reminder yang ingin dihapus: ")) - 1
            manager.delete_reminder(index)
        elif choice == "4":
            manager.display_reminders()
        elif choice == "5":
            print("Keluar dari aplikasi.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")