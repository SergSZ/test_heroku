import random
import json

times = ["утром", "днём", "вечером", "ночью", "после обеда", "перед сном"]
advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
promises = ["гостей из забытого прошлого", "встреч со старыми знакомыми", "неожиданного праздника", "приятных перемен"]
prophecies_list = {}
prophecies = ''

generated_prophecies = []
for j in range(0,6):
    one_prophecie = random.choice(times).capitalize()+" "+random.choice(advices).lower()+" "+random.choice(promises).lower()
    generated_prophecies.append(one_prophecie.rstrip(' '))


prophecies_list["prophecies"] = generated_prophecies


prophecies = json.dumps(prophecies_list, sort_keys=False, indent=3)
print(prophecies)
