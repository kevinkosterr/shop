from django.db import IntegrityError, transaction


def _update_or_create(self, **kwargs):
    """Update or create the record."""
    assert kwargs, "Function update_or_create requires at least one keyword argument."

    obj, created = self.get_or_create(**kwargs)
    defaults = kwargs.pop('defaults', {})
    if created:
        return obj, True, False
    else:
        try:
            params = dict([(k, v) for k, v in kwargs.items() if '__' not in k])
            params.update(defaults)
            for attr, val in params.items():
                if hasattr(obj, attr):
                    setattr(obj, attr, val)
            sid = transaction.savepoint()
            obj.save(force_update=True)
            transaction.savepoint_commit(sid)
            return obj, False, True
        except IntegrityError as e:
            transaction.savepoint_rollback(sid)
            try:
                return self.get(**kwargs), False, False
            except self.model.DoesNotExist:
                raise e
