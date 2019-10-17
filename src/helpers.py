import numpy as np
import pandas as pd

def unnest_transcripts(events, values):
    offer_ids = []
    amounts = []
    rewards = []

    for event, value in zip(events, values):
    
        if event in ["offer viewed", "offer received"]:
            offer_ids.append(value.get("offer id"))
            amounts.append(np.nan)
            rewards.append(np.nan)
        elif event == "transaction":
            offer_ids.append(np.nan)
            amounts.append(value.get("amount"))
            rewards.append(np.nan)
        elif event == "offer completed":
            offer_ids.append(value.get("offer_id"))
            amounts.append(np.nan)
            rewards.append(value.get("reward"))
        else:
            offer_ids.append(np.nan)
            amounts.append(np.nan)
            rewards.append(np.nan)
            
    return offer_ids, amounts, rewards