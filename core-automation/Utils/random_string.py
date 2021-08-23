import string
import random

__letters = string.ascii_lowercase


def generate_random_agency():
    randstr = (''.join(random.choice(__letters) for _ in range(6)))
    return 'Agency'+'_'+randstr

def generate_agency_admin_lname():
    randstr = (''.join(random.choice(__letters) for _ in range(6)))
    return randstr

def generate_agency_admin():
    randstr = (''.join(random.choice(__letters) for _ in range(6)))
    return 'agencyAdmin'+'_'+randstr+'@adcuratio.com'

def generate_random_advertiser():
    randstr = (''.join(random.choice(__letters) for _ in range(6)))
    return 'Advertiser'+" "+randstr

def generate_advertiser_admin():
    randstr = (''.join(random.choice(__letters) for _ in range(6)))
    return 'advAdmin'+'_'+randstr+'@adcuratio.com'

def generate_random_brand():
    randstr = (''.join(random.choice(__letters) for _ in range(6)))
    return 'Brand'+'_'+randstr

def generate_random_subbrand():
    randstr = (''.join(random.choice(__letters) for _ in range(6)))
    return 'SubBrand'+'_'+randstr

def generate_random_phone():
    phone_num = random.randint(5000000000, 9999999999)
    return phone_num

def generate_rand_creative_name(creative_name):
    randstr = (''.join(random.choice(__letters) for _ in range(6)))
    return creative_name + '_' + randstr

def generate_rand_creative_isci(creative_name):
    phone_num = random.randint(500000, 999999)
    return creative_name+'_'+str(phone_num)