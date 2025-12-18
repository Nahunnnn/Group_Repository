import Igbo_Aaron
import Hausa_Nanret
import Yoruba_Ifee
import Edo_Nahum
import tiv_dicctionary


print("--- NIGERIAN LANGUAGE TRANSLATOR ---")
print("Select a Language:")
print("1. Edo")
print("2. Hausa")
print("3. Yoruba")
print("4 Igbo")
print("5. Tiv")

choice = input("Enter your choice (1-5):")

word = input("Enter an English word:")

if choice == "1":
    print("Igbo Translation:", Igbo_Aaron.translate(word))
elif choice == "2":
    print("Hausa Translation:", Hausa_Nanret.translate(word))
elif choice == "3":
    print("Yoruba Translation:", Yoruba_Ifee.translate(word))
elif choice == "4":
    print("Edo Translation:", Edo_Nahum.translate(word))
elif choice == "5":
    print("Tiv Translation:", Tiv_Kelvin.translate(word))
else:
    print("Invalid choice")







