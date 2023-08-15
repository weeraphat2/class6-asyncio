# Asynchronous programming of making breakfast.

Demonstrates asynchronous programming in Python using an example of making breakfast. Suppose we have the following instructions to make a breakfast.

- Pour coffee.
- Heat a pan and fry two eggs.
- Toast 2 slices of bread.
- Add butter to toast.

There are two ways you can execute these instructions 
1. in the first method, you do each these steps sequentially that is you pour a cup of coffee, then heat the pan and fry the eggs. You wait for the eggs to be ready and then you toast the bread and finally add butter to toast.

Now, if you have cooking experience you will execute some of the steps in this instruction concurrently.

2. So you start by pouring a cup of coffee, then you heat a pan and while the pan is heating you put a slice of bread in the toaster. Then you crack two eggs in the pan. So now you have the eggs and toast cooking at the same time. When the toast is ready you take that out and put another bread in the toaster. You then apply butter on the first toasted bread and move on to take the fried eggs. When the second slice of bread is toasted you apply butter on it and breakfast is ready

! So basically you switch your attention between toasting bread and frying eggs thereby reducing the overall time required to prepare the breakfast.

Compared to the first method, it takes less time to cook your breakfast this way. In the second method, multiple tasks are carried out at the same time and you switch between tasks whenever your current task doesn't need your attention. This is the concept of asynchronous programming.

Start by creating empty classes for each of the breakfast item.

```python
class Coffee:
   pass
class Egg:
   pass
class Toast:
   pass
```

Next, we define the tasks. The first task is to pour coffee. This is not an asycnhronous task, in other words we cannot do anything else while pouring coffee. So let's define this task as a normal function. All this function does is to print the message Pouring coffee

```python
def PourCoffee():
   print("Pouring coffee")
   return Coffee()
```

The second step is to fry two eggs, which can be done concurrently while toasting the bread. Therefore this task can be defined as a coroutine.

```python
async def FryEggsAsync(howMany):
    print("Heat pan to fry eggs")
    await asyncio.sleep(3)
    print("Frying",howMany,"eggs")
    await asyncio.sleep(3)
    print("Eggs are ready")
    return Egg()
 ```

 The final two steps in the instruction is to toast each slice of the bread and apply butter on toast. These two steps are related but applying the butter can be done only after the bread is toasted. Therefore these two steps have to be performed sequentially but can be done in parallel with frying eggs.

 ```python
 async def ApplyButter():
    print("Spreading butter on toast")
    await asyncio.sleep(1)
    
async def ToastAsync(slices):
    for slice in range(slices):
      print("Toasting bread", slice + 1)
      await asyncio.sleep(3)
      print("Bread", slice + 1, "toasted")
      await ApplyButter()
      print ("Toast", slice + 1, "ready")
    return Toast()
```

The two async tasks, i.e, FryEggsAsync() and ToastAsync() can be run concurrently using the function **asyncio.gather()**.

```python
 await asyncio.gather(FryEggsAsync(2),ToastAsync(2))
```

Putting all these pieces of code together, we have the full program as below.

```python
import asyncio
import time

class Coffee:
    pass
class Egg:
    pass
class Toast:
    pass

def PourCoffee():
    

async def ApplyButter():
    
  
async def FryEggsAsync(howMany):
    

async def ToastAsync(slices):
    

async def main():
    
    
if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{time.ctime()} - Breakfast cooked in",elapsed,"seconds.")
 ```

 result
 ```
Tue Aug  1 22:30:43 2023 - Pouring coffee
Tue Aug  1 22:30:43 2023 - Coffee is ready
Tue Aug  1 22:30:43 2023 - Heat pan to fry eggs
Tue Aug  1 22:30:43 2023 - Toasting bread 1
Tue Aug  1 22:30:46 2023 - Pan is ready
Tue Aug  1 22:30:46 2023 - Frying 2 eggs
Tue Aug  1 22:30:46 2023 - Bread 1 toasted
Tue Aug  1 22:30:46 2023 - Spreading butter on toast
Tue Aug  1 22:30:47 2023 - Toast 1 ready
Tue Aug  1 22:30:47 2023 - Toasting bread 2
Tue Aug  1 22:30:49 2023 - Eggs are ready
Tue Aug  1 22:30:50 2023 - Bread 2 toasted
Tue Aug  1 22:30:50 2023 - Spreading butter on toast
Tue Aug  1 22:30:51 2023 - Toast 2 ready
Tue Aug  1 22:30:51 2023 - Breakfast cooked in 8.00863425 seconds.
```