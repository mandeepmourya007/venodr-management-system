from purchase_order.models import PurchaseOrder
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
@receiver(post_save, sender=PurchaseOrder)
def update_vendor_performance_metrics_on_po_save(sender, instance, created, **kwargs):
    if created or instance.status == 'completed' or 'quality_rating' in instance.changed_fields or 'acknowledgment_date' in instance.changed_fields:
        instance.vendor.update_performance_metrics()

@receiver(post_delete, sender=PurchaseOrder)
def update_vendor_performance_metrics_on_po_delete(sender, instance, **kwargs):
    instance.vendor.update_performance_metrics()