import praw

def newRedditInterface():
  r = praw.Reddit(user_agent='unsaver v0.1 by /u/snarkyxanf')
  r.login('','')
  return r

def unsave(r, count):
  total = 0
  saved = r.user.get_saved(limit=count)
  for item in saved:
    try:
      total = total + 1
      print('Unsaving no', total, '...', item.fullname, str(item))
      item.unsave()
    except AttributeError as err:
      print(err)


if __name__ == "__main__":
  r = newRedditInterface()

  count = int(input("Enter number of items to delete: "))

  unsave(r, count)
