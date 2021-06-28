import tidalapi
import requests
from tqdm import tqdm

def init_session():
  session = tidalapi.Session()
  session.login_oauth_simple()
  return session

def get_tracks(session):
  return tidalapi.Favorites(session, session.user.id).tracks()

def add_tracks(session, tracks):
  favorites = tidalapi.Favorites(session, session.user.id)

  print('Copying tracks...')
  for i in tqdm(range(len(tracks))):
    try:
      favorites.add_track(tracks[i].id)
    except requests.exceptions.HTTPError:
      print("Skipping missing track")

print("Log in to the source account")
tracks = get_tracks(init_session())

print("Log in to the destination account")
add_tracks(init_session(), tracks)



