def sessionsQuery(**options):
  """
  A function that returns the string formatted API query for Arkime v3.x.
  
  PARAMETERS
  ----------
  date_range, numerical expression of hours, -1 is the default for all time
  expresssion, a string search expression
  facets, numerical flag to include data for maps and timeline graphs
  length, number of items to return, default is 100 and max is 2,000,000
  start, specifies which entry to start from
  startTime, Unix EPOC formatted timestamp that specifies the starting point for the query
  stopTime,  Unix EPOC formatted timestamp that specifies the stopping point for the query
  view, the view name to apply before the expression
  order, a comma seperated list of field names to sort on, can be followed by :asc or :desc
  fields, a comma seperated list of fields to return
  bounding, queries data based on different aspects of session time, \
            options are first, last, both, either, or database
  strictly, specifies the entire session must be within the date range specified

  RETURNS
  ----------
  A formatted string
  """
  try:
    date_range = int(options.get("date_range", "-1"))
    expression = str(options.get("expression", None))
    facets = int(options.get("facets", None)) #Default of 0
    length = int(options.get("length", None)) #Defualt of 100
    start = int(options.get("start", None))
    startTime = int(options.get("startTime", None))
    stopTime = int(options.get("stopTime", None))
    view = str(options.get("view", None))
    order = str(options.get("order", None))
    fields = str(options.get("fields", None))
    bounding = str(options.get("bounding", None)) #Default of last.  Can be first/last/both.
    strictly = bool(options.get("strictly", None)) #Default of false
  except:
    return(1, "sessionsQuery received an invalid data type")

    api_call = ""

    if startTime and stopTime:
      if (startTime) < (stopTime):
        api_call += "startTime={}&stopTime={}&".format(startTime, stopTime)
      else:
        return(1, "stopTime value must be greater than startTime value.")
    else:
      api_call += "date={}&".format(date_range)

    
    if view:
      api_call += "view={}&".format(view)
    if expression:
      api_call += "expression={}&".format(expression)
    if facets:
      api_call += "facets={}&".format(facets)
    if length:
      api_call += "length={}&".format(length)
    if start:
      api_call += "start={}&".format(start)
    if order:
      api_call += "order={}&".format(order)
    if fields:
      api_call += "fields={}&".format(fields)
    if bounding:
      api_call += "bounding={}&".format(bounding)
    if strictly:
      api_call += "strictly={}&".format(strictly)

    return(api_call)