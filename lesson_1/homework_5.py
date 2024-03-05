import asyncio
import json

async def read_data(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            print(f"Data read from {filename}: {data}")
            return data
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return None

async def write_data(filename, data):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file)
            print(f"Data written to {filename}: {data}")
    except Exception as e:
        print(f"Error writing to {filename}: {e}")

async def main():
    data_1_task = asyncio.create_task(read_data('data_1.json'))
    data_1 = await data_1_task

    if data_1:
        await write_data('data_2.json', data_1)

asyncio.run(main())








