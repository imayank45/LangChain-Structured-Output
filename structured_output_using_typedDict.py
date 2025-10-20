from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional

load_dotenv()

model = ChatOpenAI()

# schema
class Review(TypedDict):
    key_themes: Annotated[list[str], 'Write down all key themes discussed in the review in a list']
    summary: Annotated[str, 'A brief summary of the review']
    sentiment: Annotated[str, 'Return sentiment of the review either negative, positive, newutral']
    pros: Annotated[Optional[list[str]], 'Write down all pros inside a list']
    cons: Annotated[Optional[list[str]], 'Write down all cons inside a list']
    name: Annotated[Optional[str], 'Write the name of reviewer']
    
    
structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""
                      Hi I am Mayank, I purchased these wireless headphones about a month ago, hoping for a good balance between sound quality and comfort. Unfortunately, my experience has been quite disappointing. The sound output is average at best — the bass is weak, and the treble often distorts at higher volumes. The Bluetooth connection frequently drops, even when my phone is right next to me. The build feels flimsy, and the ear cushions started wearing out within a couple of weeks.Battery life was advertised as 20 hours, but in reality, it barely lasts 10–12 hours on a full charge. What’s worse, the charging port feels loose, making it hard to charge properly. The only decent aspect is the design — it looks modern and lightweight, but that’s not enough to make up for its poor performance and reliability. Overall, this product failed to deliver on most of its promises.

✅ Pros:

Lightweight and stylish design

Comfortable for short use

Easy Bluetooth pairing

❌ Cons:

Poor sound quality and weak bass

Bluetooth connection drops frequently

Battery life is much shorter than advertised

Fragile build and uncomfortable for long sessions

Charging port feels loose and unreliable
                      """)

print(result)
print(result['summary'])
print(result['sentiment'])