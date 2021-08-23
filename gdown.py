# get the shared link of data
# https://drive.google.com/uc?id=1ImZGCZ9TF_xIjw7n693qOo8VXTJXbAIJ
# then gat id and pest it hear
!gdown --id 1ImZGCZ9TF_xIjw7n693qOo8VXTJXbAIJ

# and store it in url
url = 'https://drive.google.com/uc?id=1ImZGCZ9TF_xIjw7n693qOo8VXTJXbAIJ'
# and you can access url 
data = pd.read_csv(url)
