import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'academicpeak.settings')
django.setup()
from tabulate import tabulate
from university.models import University
import pandas as pd


def print_university():
    """Print the universities in the database"""
    universities = University.objects.all().order_by('university_rank')
    university_data = []
    for uni in universities:
        university_data.append(
            [uni.university_rank, uni.university_name, uni.university_country, uni.university_global_score,
             uni.university_enrollment, uni.university_link, uni.university_photo_link])
    # print(university_data)
    table_headers = ["Rank", "University Name", "Country", "Global Score", "Enrollment", "Link", "Photo Link"]
    print(tabulate(university_data, headers=table_headers, tablefmt="grid"))


def return_university_list():
    """Return the universities in the database"""
    universities = University.objects.all().order_by('university_rank')
    university_data = []
    for uni in universities:
        university_data.append(
            [uni.university_rank, uni.university_name, uni.university_country, uni.university_global_score,
             uni.university_enrollment, uni.university_link, uni.university_photo_link])
    return (university_data)


def return_university_dict():
    """Return the universities in the database as a dictionary"""
    universities = University.objects.all().order_by('university_rank')
    university_data = {}
    for uni in universities:
        university_dict = {
            "Rank": uni.university_rank,
            "University_Name": uni.university_name,
            "Country": uni.university_country,
            "Global_Score": uni.university_global_score,
            "Enrollment": uni.university_enrollment,
            "Link": uni.university_link,
            "Photo_Link": uni.university_photo_link
        }
        university_data[uni.university_rank] = university_dict
    return university_data


def return_university_table():
    """Return the universities in the database as a table"""
    universities = University.objects.all().order_by('university_rank')
    university_data = []
    for uni in universities:
        university_data.append(
            [uni.university_rank, uni.university_name, uni.university_country, uni.university_global_score,
             uni.university_enrollment, uni.university_link, uni.university_photo_link])
    # print(university_data)
    table_headers = ["Rank", "University Name", "Country", "Global Score", "Enrollment", "Link", "Photo Link"]
    return (tabulate(university_data, headers=table_headers, tablefmt="grid"))


def import_university_form_excel(excel_path):
    """Import the excel file to the database"""
    excel_name = os.path.basename(excel_path)
    user_confirm = input(f"add or overwritten the database by this excel({excel_name}) (add/over): ")
    if user_confirm == 'over':
        user_confirm = input(f"The database will be overwritten by this excel({excel_name}) (y/n): ")
        if user_confirm == 'y':
            delete_all_universities()
            print(f'The database has been cleared.')
            print(f'Importing {excel_name} to the database.')
            df = pd.read_excel(excel_path)
            for index, row in df.iterrows():
                university_rank = row['Rank']
                university_name = row['University Name']
                university_country = row['Country']
                university_global_score = row['Global Score']
                university_enrollment = row['Enrollment']
                university_link = row['Link']
                university_photo_link = row['Photo Link']
                university = University.objects.create(university_rank=university_rank,
                                                       university_name=university_name,
                                                       university_country=university_country,
                                                       university_global_score=university_global_score,
                                                       university_enrollment=university_enrollment,
                                                       university_link=university_link,
                                                       university_photo_link=university_photo_link
                                                       )
                print(f'Added {university_name} to the database.')
            print(f'Imported {excel_name} to the database.')
            print(f'Adjusting the university rank...')
            adjust_university_rank()
            print(f'Current university rank.')
            print_university()
        else:
            print(f'Canceled.')
            return None
    else:
        print(f'Add {excel_name} to the database.')
        df = pd.read_excel(excel_path)
        for index, row in df.iterrows():
            university_rank = row['Rank']
            university_name = row['University Name']
            university_country = row['Country']
            university_global_score = row['Global Score']
            university_enrollment = row['Enrollment']
            university_link = row['Link']
            university_photo_link = row['Photo Link']
            university = University.objects.create(university_rank=university_rank,
                                                   university_name=university_name,
                                                   university_country=university_country,
                                                   university_global_score=university_global_score,
                                                   university_enrollment=university_enrollment,
                                                   university_link=university_link,
                                                   university_photo_link=university_photo_link, )
            print(f'Added {university_name} to the database.')
        print(f'Imported {excel_name} to the database.')
        print(f'Adjusting the university rank...')
        adjust_university_rank()
        print(f'Current university rank.')
        print_university()


def delete_all_universities():
    """Delete all universities in the database."""
    universities = University.objects.all()
    universities.delete()
    print(f'Deleted all universities in the database.')


def add_university_input():
    """Add a new university to the database."""
    print(f'Adding a new university to the database.')
    university_rank = input("university_rank: ")
    university_name = input("university_name: ")
    university_country = input("university_country: ")
    university_global_score = input("university_global_score: ")
    university_enrollment = input("university_enrollment: ")
    university_link = input("university_link: ")
    university_photo_link = input("university_photo_link: ")
    university = University.objects.create(university_rank=university_rank,
                                           university_name=university_name,
                                           university_country=university_country,
                                           university_global_score=university_global_score,
                                           university_enrollment=university_enrollment,
                                           university_link=university_link,
                                           university_photo_link=university_photo_link, )
    adjust_university_rank()
    print(f'Added {university_name} to the database.')


def adjust_university_rank():
    """Adjust the university rank based on the global score."""
    universities = University.objects.all().order_by('-university_global_score')
    rank = 1
    for uni in universities:
        uni.university_rank = rank
        uni.save()
        rank += 1
    universities = University.objects.all().order_by('university_rank')


if __name__ == '__main__':
    try:
        excel_path = r''
        import_university_form_excel(excel_path)
    except Exception as e:
        print(f'Error: {e}')