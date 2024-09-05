total_purchase = float(input("Enter the total purchase: "))
is_student = input("Do You Student? (ya/tidak): ") == 'ya'

total_final = (total_purchase * 0.8 * 1.05) if is_student else (total_purchase * 1.05)

print(f"Jumlah akhir: {total_final:.2f}")