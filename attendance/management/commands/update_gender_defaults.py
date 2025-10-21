from django.core.management.base import BaseCommand
from attendance.models import Farmer, Student


class Command(BaseCommand):
    help = 'Update all existing records with null/empty gender to default "Other"'

    def handle(self, *args, **options):
        # Update Farmers
        farmers_updated = Farmer.objects.filter(gender__isnull=True).update(gender='O')
        farmers_empty = Farmer.objects.filter(gender='').update(gender='O')
        
        # Update Students
        students_updated = Student.objects.filter(gender__isnull=True).update(gender='O')
        students_empty = Student.objects.filter(gender='').update(gender='O')
        
        total_farmers = farmers_updated + farmers_empty
        total_students = students_updated + students_empty
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully updated {total_farmers} farmers and {total_students} students to have "Other" as default gender.'
            )
        )
