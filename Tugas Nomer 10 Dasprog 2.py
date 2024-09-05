def adjust_baking_time(base_time, is_double_size):
    return int(base_time * 1.5) if is_double_size else base_time

def bread_machine(bread_type, is_double_size, manual_bake):
    times = {
        'W': (15, 60, 15, 35),  
        'S': (20, 75, 20, 45)   
    }
    
    if bread_type in times:
        mix, rise, shape, bake = times[bread_type]
        print(f"{'White' if bread_type == 'W' else 'Sweet'} Bread Selected.")
        print(f"Mixing for {mix} minutes.")
        print(f"Rising for {rise} minutes.")
        print(f"Shaping for {shape} minutes.")
        if manual_bake:
            print("Manual baking selected. Please remove dough for manual baking.")
        else:
            bake_time = adjust_baking_time(bake, is_double_size)
            print(f"Baking for {bake_time} minutes.")
    else:
        print("Invalid bread type.")

bread_type = input("Enter bread type (W for White, S for Sweet): ").upper()
is_double_size = input("Is the loaf size double? (Y/N): ").upper() == 'Y'
manual_bake = input("Is the baking manual? (Y/N): ").upper() == 'Y'

bread_machine(bread_type, is_double_size, manual_bake)