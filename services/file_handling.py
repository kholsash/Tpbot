from data.requests import get_answers

async def answrs(category5_id):
    all_answers= await get_answers(category5_id)
    for answr in all_answers:
        text += str(answr.description)
    return text
