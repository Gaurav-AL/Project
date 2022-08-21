def getInfo(number , operator , circle):
    if(operator == 'Airtel' and circle == 'Delhi NCR'):
        return getAirtelDelhiNCRPlans()
    if(operator == 'Idea' and circle == 'Delhi NCR'):
        return getIdeaDelhiNCRPlans()
    if(operator == 'Vodafone' and circle == 'Delhi NCR'):
        return getVodafoneDelhiNCRPlans()
    if(operator == 'Jio' and circle == 'Delhi NCR'):
        return getjioDelhiNCRPlans()
    else:
        return getDefaultPlans()

def getAirtelDelhiNCRPlans():
    plans = [['Amount : 3359' ,'Data : 2.5BG' , 'Validity  : 365 days'] , ['Amount : 2999', 'Data : 2GB' , 'Validity  : 365 days']
             ,['Amount : 1799', 'Data : 24GB' , 'Validity  : 365 days'],['Amount : 999', 'Data : 2.5GB' , 'Validity  :84 days'],
             ['Amount :839', 'Data : 2GB' , 'Validity  : 84 days']]
    return plans

def getIdeaDelhiNCRPlans():
    plans = [['Amount : 3359' ,'Data : 2.5BG' , 'Validity  : 365 days'] , ['Amount : 2999', 'Data : 2GB' , 'Validity  : 365 days']
             ,['Amount : 1799', 'Data : 24GB' , 'Validity  : 365 days'],['Amount : 999', 'Data : 2.5GB' , 'Validity  :84 days'],
             ['Amount :839', 'Data : 2GB' , 'Validity  : 84 days']]
    return plans

def getVodafoneDelhiNCRPlans():
    plans = [['Amount : 3359' ,'Data : 2.5BG' , 'Validity  : 365 days'] , ['Amount : 2999', 'Data : 2GB' , 'Validity  : 365 days']
             ,['Amount : 1799', 'Data : 24GB' , 'Validity  : 365 days'],['Amount : 999', 'Data : 2.5GB' , 'Validity  :84 days'],
             ['Amount :839', 'Data : 2GB' , 'Validity  : 84 days']]
    return plans

def getjioDelhiNCRPlans():
    plans = [['Amount : 3359' ,'Data : 2.5BG' , 'Validity  : 365 days'] , ['Amount : 2999', 'Data : 2GB' , 'Validity  : 365 days']
             ,['Amount : 1799', 'Data : 24GB' , 'Validity  : 365 days'],['Amount : 999', 'Data : 2.5GB' , 'Validity  :84 days'],
             ['Amount :839', 'Data : 2GB' , 'Validity  : 84 days']]
    return plans

def getDefaultPlans():
    plans = [['Amount : 3359' ,'Data : 2.5BG' , 'Validity  : 365 days'] , ['Amount : 2999', 'Data : 2GB' , 'Validity  : 365 days']
             ,['Amount : 1799', 'Data : 24GB' , 'Validity  : 365 days'],['Amount : 999', 'Data : 2.5GB' , 'Validity  :84 days'],
             ['Amount :839', 'Data : 2GB' , 'Validity  : 84 days']]
    return plans




    