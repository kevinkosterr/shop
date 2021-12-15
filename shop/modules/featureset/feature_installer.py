from datetime import datetime
from rich import print as rprint

from shop.models import Feature
from . import FeatureInstallError


def feature(name: str, author: str, contact=None, reference=None):
    """Decorator used to mark a feature. This will make sure the feature is installed on the application."""

    def decorator(feat):

        feature_record = Feature.objects.get(name=name)

        if not feature_record or feature_record.installed is False:
            # Install the feature, because it wasn't found in the database, or it was never installed.
            try:
                rprint("Installing %(name)s into database..." % {"name": name})
                installed = bool(feat())
            except FeatureInstallError as e:
                # If there's an installation error, print the error and return false to indicate that the feature hasn't
                # been installed.
                installed = False
                rprint(e)
                return False
            finally:
                # Always create or update a record after trying the installation, this way we can keep track of the
                # features that have been installed and those that weren't.
                new_feature, created, updated = Feature.objects.update_or_create(
                    name=name,
                    author=author,
                    contact=contact,
                    reference=reference,
                    installation_ts=None if not installed else datetime.now(),
                    installed=installed,
                )
                rprint(
                    f"Feature with name: {name} [{new_feature}]: \n created: {created}, updated: {updated}"
                )
        else:
            # Feature is already installed here. Skipping installation..
            rprint("Feature %(name)s already installed." % {"name": name})

        return True

    return decorator
