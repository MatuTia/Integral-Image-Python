import numpy as np
import os.path
import string

from PIL import Image
from asyncio import gather, create_task


def image_loader(path: string) -> list[np.ndarray]:
    return [np.array(Image.open(os.path.join(path, file)).convert('L'), dtype=np.int64) for file in os.listdir(path)]


async def loader(path: string) -> np.ndarray:
    return np.array(Image.open(path).convert('L'), dtype=np.int64)


async def parallel_image_loader(path: string) -> list[np.ndarray]:
    to_load = [create_task(loader(os.path.join(path, file))) for file in os.listdir(path)]
    return await gather(*to_load)
