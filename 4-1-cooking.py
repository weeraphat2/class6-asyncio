import asyncio
import time

class Coffee:
    pass
class Egg:
    pass
class Toast:
    pass

def PourCoffee():
    print(f"{time.ctime()} - Pouring coffee")
    return Coffee()

async def ApplyButter():
    print(f"{time.ctime()} - Spreading butter on toast")
    await asyncio.sleep(1)

  
async def FryEggsAsync(howMany):
    print(f"{time.ctime()} - Heat pan to fry eggs")
    await asyncio.sleep(3)
    print(f"{time.ctime()} - Frying",howMany,"eggs")
    await asyncio.sleep(3)
    print(f"{time.ctime()} - Eggs are ready")
    return Egg()

async def ToastAsync(slices):
    for slice in range(slices):
      print(f"{time.ctime()} - Toasting bread", slice + 1)
      await asyncio.sleep(3)
      print(f"{time.ctime()} - Bread", slice + 1, "toasted")
      await ApplyButter()
      print (f"{time.ctime()} - Toast", slice + 1, "ready")
    return Toast()

async def main():
    cup = PourCoffee()
    print(f"{time.ctime()}- Coffee is ready")
    await asyncio.gather(FryEggsAsync(2),ToastAsync(2))
    
if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{time.ctime()} - Breakfast cooked in",elapsed,"seconds.")

# Tue Aug 15 22:19:18 2023 - Pouring coffee
# Tue Aug 15 22:19:18 2023- Coffee is ready
# Tue Aug 15 22:19:18 2023 - Heat pan to fry eggs
# Tue Aug 15 22:19:18 2023 - Toasting bread 1
# Tue Aug 15 22:19:21 2023 - Frying 2 eggs
# Tue Aug 15 22:19:21 2023 - Bread 1 toasted
# Tue Aug 15 22:19:21 2023 - Spreading butter on toast
# Tue Aug 15 22:19:22 2023 - Toast 1 ready
# Tue Aug 15 22:19:22 2023 - Toasting bread 2
# Tue Aug 15 22:19:24 2023 - Eggs are ready
# Tue Aug 15 22:19:25 2023 - Bread 2 toasted
# Tue Aug 15 22:19:25 2023 - Spreading butter on toast
# Tue Aug 15 22:19:26 2023 - Toast 2 ready
# Tue Aug 15 22:19:26 2023 - Breakfast cooked in 8.043516499998077 seconds.