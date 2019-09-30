from requests_oauthlib import OAuth2Session

graph_url = 'https://graph.microsoft.com/v1.0'

def get_user(token):
  graph_client = OAuth2Session(token=token)
  # Send GET to /me
  user = graph_client.get('{0}/me'.format(graph_url))
  # Return the JSON result
  return user.json()

def get_calendar_events(token):
  graph_client = OAuth2Session(token=token)

  # Configure query parameters to
  # modify the results
  query_params = {
    '$select': 'subject,organizer,start,end',
    '$orderby': 'createdDateTime DESC'
  }

  # Send GET to /me/events
  events = graph_client.get('{0}/me/events'.format(graph_url), params=query_params)
  # Return the JSON result
  return events.json()

def get_onedrive_details(token):
  graph_client = OAuth2Session(token=token)

  # Configure query parameters to
  # modify the results
  query_params = {
    '$select': 'id,driveType,owner,quota',
    '$orderby': 'createdDateTime DESC'
  }

  # Send GET to /me/events
  events = graph_client.get('{0}/me/drive'.format(graph_url), params=query_params)
  # Return the JSON result
  return events.json()

def get_onedrive_directory(token):
  graph_client = OAuth2Session(token=token)

  # Configure query parameters to
  # modify the results
  query_params = {
    '$select': 'value',
    # '$orderby': 'createdDateTime DESC'
  }

  # Send GET to /me/events
  events = graph_client.get('{0}/me/drive/sharedWithMe'.format(graph_url))
  # Return the JSON result
  return events.json()

def get_directory_contents(token):
  graph_client = OAuth2Session(token=token)

  # Configure query parameters to
  # modify the results
  query_params = {
    '$select': 'value',
    # '$orderby': 'createdDateTime DESC'
  }

  # Send GET to /me/events

  # This works, my personal drive
  # events = graph_client.get('{0}/me/drive/items/01ELAC4DN6Y2GOVW7725BZO354PWSELRRZ'.format(graph_url))

  # this does not work
  # events = graph_client.get('{0}/me/drive/items/01ELAC4DILBDZMIXN5J5A32ACBYPBN4B2N/children'.format(graph_url))

  events = graph_client.get('{0}/users/58639a68-e427-42b4-ab92-7df6198c1687/drive/items/01ELAC4DILBDZMIXN5J5A32ACBYPBN4B2N/children'.format(graph_url))

  # This works, my drive
  # events = graph_client.get('{0}/users/58639a68-e427-42b4-ab92-7df6198c1687/drive/items/01ELAC4DN6Y2GOVW7725BZO354PWSELRRZ'.format(graph_url))

  # This works, my drive, this does nothing
  # events = graph_client.get('{0}/users/58639a68-e427-42b4-ab92-7df6198c1687/drive/items/01ELAC4DN6Y2GOVW7725BZO354PWSELRRZ/children'.format(graph_url))

  # This works, my drive
  # events = graph_client.get('{0}/drives/b!pcvrKCqIeUKX7KFnRi0AC4UDAMUVdyZGp3Y-2yztnzchcY6hxph1S6l9aQESUTwn/items/01ELAC4DN6Y2GOVW7725BZO354PWSELRRZ'.format(graph_url))

  # This does not work, no children
  # events = graph_client.get('{0}/drives/b!pcvrKCqIeUKX7KFnRi0AC4UDAMUVdyZGp3Y-2yztnzchcY6hxph1S6l9aQESUTwn/items/01ELAC4DILBDZMIXN5J5A32ACBYPBN4B2N/children'.format(graph_url))

  # This does not work, no children
  # events = graph_client.get('{0}/users/58639a68-e427-42b4-ab92-7df6198c1687/drive/items/01ELAC4DN6Y2GOVW7725BZO354PWSELRRZ/children'.format(graph_url))

  # Return the JSON result
  return events.json()
