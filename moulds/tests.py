from django.test import TestCase

# Create your tests here.

from .models import Mould

class MouldCounterTest(TestCase):

    def test_initial_closures(self):
        mould = Mould.objects.create(
            number="TEST-001",
            name="Test Mould",
            cavities_total=32,
            cavities_active=32,
            initial_closures=1_000_000,
        )

        self.assertEqual(mould.total_closures,
                         1_000_000,
        
        )

    def test_initial_closures_correction(self):
        mould = Mould.objects.create(
            number="TEST-002",
            name="Test Mould Correction",
            cavities_total=32,
            initial_closures=1_000_000,
        )

        Mould.objects.filter(pk=mould.pk).update(
            total_closures=1_005_000
        )

        mould.initial_closures = 1_200_000
        mould.save()

        self.assertEqual(
            mould.initial_closures,
            1_200_000,
        )

        self.assertEqual(
            mould.total_closures,
            1_205_000,
        )


    def test_initial_closures_partial_update(self):
        mould = Mould.objects.create(
            number="TEST-003",
            name="Test Mould Partial Update",
            cavities_total=32,
            initial_closures=500_000,
        )

        Mould.objects.filter(pk=mould.pk).update(
            total_closures=501_000
        )

        mould.initial_closures = 600_000

        mould.save(update_fields=["initial_closures"])

        mould.refresh_from_db()

        self.assertEqual(mould.initial_closures, 600_000)
        self.assertEqual(mould.total_closures, 601_000)

    def test_edit_mould_does_not_reset_counter(self):
        mould = Mould.objects.create(
            number="TEST-004",
            name="Test Mould Edit",
            cavities_total=32,
            initial_closures=500_000,
        )

        Mould.objects.filter(pk=mould.pk).update(
            total_closures=505_000
        )

        mould.name = "Test Mould Edit 2"
        mould.save()

        mould.refresh_from_db()

        self.assertEqual(mould.name, "Test Mould Edit 2")
        self.assertEqual(mould.total_closures, 505_000)
        