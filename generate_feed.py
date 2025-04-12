import requests
from bs4 import BeautifulSoup

# Replace this URL with the one for your show
url = "https://gsradio.net/shows/divided_kingdom/"

# Fetch the page
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all audio links (You may need to adjust this if the structure changes)
audio_links = soup.find_all('a', href=True)
audio_urls = [link['href'] for link in audio_links if link['href'].endswith('.mp3')]

# Create RSS Feed
rss_content = '''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
    <title>Divided Kingdom Podcast</title>
    <link>https://gsradio.net/shows/divided_kingdom/</link>
    <description>Episodes of the Divided Kingdom show</description>
    <language>en-us</language>'''

for audio_url in audio_urls:
    rss_content += f'''
    <item>
        <title>Episode</title>
        <link>{audio_url}</link>
        <enclosure url="{audio_url}" type="audio/mp3" />
        <guid>{audio_url}</guid>
        <pubDate>Mon, 01 Jan 2025 00:00:00 GMT</pubDate>
    </item>'''

rss_content += '''
</channel>
</rss>'''

# Save the RSS feed to a file
with open("feed.xml", "w") as f:
    f.write(rss_content)
