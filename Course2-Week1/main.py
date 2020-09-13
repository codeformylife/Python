text = "X-DSPAM-Confidence:    0.8475";
start = text.find(":") 
end = len(text)
temp = text[start+1:end]
result = float(temp.strip())
print(result)
       