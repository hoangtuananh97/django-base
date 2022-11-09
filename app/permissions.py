from enum import Enum
from typing import Iterable, List

from django.contrib.auth.models import Permission


class BasePermissionEnum(Enum):
    @property
    def codename(self):
        return self.value.split(".")[1]


class AccountPermissions(BasePermissionEnum):
    MANAGE_USERS = "account.manage_users"
    MAIN_MENU_FORECAST = "account.main_menu_forecast"
    MAIN_MENU_VMI = "account.main_menu_vmi"
    MAIN_MENU_DRP = "account.main_menu_drp"
    MAIN_MENU_CONFIGURATION = "account.main_menu_configuration"
    VIEW_STAFF = "account.view_staff"
    EDIT_STAFF = "account.edit_staff"
    DELETE_STAFF = "account.delete_staff"
    VIEW_PERMISSION_GROUP = "account.view_permission_group"
    EDIT_PERMISSION_GROUP = "account.edit_permission_group"
    DELETE_PERMISSION_GROUP = "account.delete_permission_group"


class AppPermission(BasePermissionEnum):
    MANAGE_APPS = "app.manage_apps"


class ChannelPermissions(BasePermissionEnum):
    MANAGE_CHANNELS = "channel.manage_channels"
    MANAGE_ALL_CHANNELS = "channel.manage_all_channels"
    MANAGE_DRAFT_CHANNELS = "channel.manage_draft_channels"


class DiscountPermissions(BasePermissionEnum):
    MANAGE_DISCOUNTS = "discount.manage_discounts"


class PluginsPermissions(BasePermissionEnum):
    MANAGE_PLUGINS = "plugins.manage_plugins"


class GiftcardPermissions(BasePermissionEnum):
    MANAGE_GIFT_CARD = "giftcard.manage_gift_card"


class MenuPermissions(BasePermissionEnum):
    MANAGE_MENUS = "menu.manage_menus"


class CheckoutPermissions(BasePermissionEnum):
    MANAGE_CHECKOUTS = "checkout.manage_checkouts"


class OrderPermissions(BasePermissionEnum):
    MANAGE_ORDERS = "order.manage_orders"


class PaymentPermissions(BasePermissionEnum):
    HANDLE_PAYMENTS = "payment.handle_payments"


class CategoryPermissions(BasePermissionEnum):
    MANAGE_ALL_CATEGORIES = "product.manage_all_categories"


class ArticleGroupingPermissions(BasePermissionEnum):
    MANAGE_ARTICLE_GROUPING = "product.manage_article_grouping"


class ProductPermissions(BasePermissionEnum):
    MANAGE_PRODUCTS = "product.manage_products"
    VIEW_DRP_PRODUCT_STATUS = "product.view_drp_product_status"
    VIEW_DRP_STO_PO_STATUS = "product.view_drp_sto_po_status"
    VIEW_DRP_STOCK_DC_RDC = "product.view_drp_stock_dc_rdc"
    VIEW_DRP_REPORT = "product.view_drp_report"
    VIEW_VMI_STOCK_AT_VENDOR = "product.view_vmi_stock_at_vendor"


class ProductTypePermissions(BasePermissionEnum):
    MANAGE_PRODUCT_TYPES_AND_ATTRIBUTES = "product.manage_product_types_and_attributes"


class ShippingPermissions(BasePermissionEnum):
    MANAGE_SHIPPING = "shipping.manage_shipping"


class SitePermissions(BasePermissionEnum):
    MANAGE_SETTINGS = "site.manage_settings"
    MANAGE_TRANSLATIONS = "site.manage_translations"


class ScgSitePermissions(BasePermissionEnum):
    VIEW_SCG_SETTINGS = "scg_site.view_scg_settings"
    EDIT_SCG_SETTINGS = "scg_site.edit_scg_settings"
    VIEW_PERIOD = "scg_site.view_period"
    EDIT_PERIOD = "scg_site.edit_period"
    VIEW_PRODUCT_CLASS_CRITERIA = "scg_site.view_product_class_criteria"
    EDIT_PRODUCT_CLASS_CRITERIA = "scg_site.edit_product_class_criteria"


class CategoryForecastPermission(BasePermissionEnum):
    VIEW_TARGET_ADJUSTMENT = "saleor_category_forecast.view_target_adjustment"
    EDIT_DRAFT_TARGET_ADJUSTMENT = (
        "saleor_category_forecast.edit_draft_target_adjustment"
    )
    EDIT_SUBMITTED_TARGET_ADJUSTMENT = (
        "saleor_category_forecast.edit_submitted_target_adjustment"
    )
    APPROVE_TARGET_ADJUSTMENT = "saleor_category_forecast.approve_target_adjustment"
    FINAL_APPROVE_TARGET_ADJUSTMENT = (
        "saleor_category_forecast.final_approve_target_adjustment"
    )


class CategoryTargetPermission(BasePermissionEnum):
    VIEW_DISPLAY_TARGET = "saleor_category_target.view_display_target"
    VIEW_TARGET_SET = "saleor_category_target.view_target_set"
    EDIT_DRAFT_TARGET_SET = "saleor_category_target.edit_draft_target_set"
    EDIT_SUBMITTED_TARGET_SET = "saleor_category_target.edit_submitted_target_set"
    APPROVE_TARGET_SET = "saleor_category_target.approve_target_set"


class FileImportPermission(BasePermissionEnum):
    MANAGE_IMPORT_FILES = "saleor_file_import.manage_import_files"


class ProductClassPermissions(BasePermissionEnum):
    VIEW_PRODUCTCLASS = "saleor_product_class.view_productclass"
    CHANGE_PRODUCTCLASS = "saleor_product_class.change_productclass"


class ProductMinMaxPermissions(BasePermissionEnum):
    VIEW_PRODUCTMINMAX = "saleor_product_min_max.view_productminmax"
    CHANGE_PRODUCTMINMAX = "saleor_product_min_max.change_productminmax"


class ProductOrderHistoryPermission(BasePermissionEnum):
    MANAGE_PRODUCT_ORDER_HISTORY = (
        "saleor_product_order_history.manage_product_order_history"  # NOQA
    )


class ProductReplacementPermissions(BasePermissionEnum):
    VIEW_PRODUCT_REPLACEMENT = "saleor_product_replacement.view_product_replacement"
    CHANGE_PRODUCT_REPLACEMENT = "saleor_product_replacement.change_product_replacement"
    DELETE_PRODUCT_REPLACEMENT = "saleor_product_replacement.delete_product_replacement"


class SupplierPermission(BasePermissionEnum):
    MANAGE_SUPPLIERS = "saleor_purchase_order.manage_suppliers"


class PurchaseOrderPermission(BasePermissionEnum):
    MANAGE_PURCHASE_ORDERS = "saleor_purchase_order.manage_purchase_orders"


class StockReplenishmentPermissions(BasePermissionEnum):
    MANAGE_STOCK_REPLENISHMENT = "saleor_stock_replenishment.manage_stock_replenishment"


class StockTransferPermissions(BasePermissionEnum):
    MANAGE_STOCKTRANSFER = "saleor_stock_transfer.manage_stocktransfer"


class ProductMasterPermissions(BasePermissionEnum):
    VIEW_PRODUCT_MASTER = "saleor_product_replacement.view_product_master"


PERMISSIONS_ENUMS = [
    AccountPermissions,
    AppPermission,
    ChannelPermissions,
    DiscountPermissions,
    PluginsPermissions,
    MenuPermissions,
    OrderPermissions,
    PaymentPermissions,
    ProductPermissions,
    ProductTypePermissions,
    ShippingPermissions,
    SitePermissions,
    CheckoutPermissions,
    ScgSitePermissions,
    CategoryPermissions,
    ArticleGroupingPermissions,
    CategoryForecastPermission,
    CategoryTargetPermission,
    FileImportPermission,
    ProductClassPermissions,
    ProductMasterPermissions,
    ProductMinMaxPermissions,
    ProductOrderHistoryPermission,
    ProductReplacementPermissions,
    SupplierPermission,
    PurchaseOrderPermission,
    StockReplenishmentPermissions,
    StockTransferPermissions,
]


def split_permission_codename(permissions):
    return [permission.split(".")[1] for permission in permissions]


def get_permissions_codename():
    permissions_values = [
        enum.codename
        for permission_enum in PERMISSIONS_ENUMS
        for enum in permission_enum
    ]
    return permissions_values


def get_permissions_enum_dict():
    return {
        enum.name: enum
        for permission_enum in PERMISSIONS_ENUMS
        for enum in permission_enum
    }


def get_permissions_from_names(names: List[str]):
    """Convert list of permission names - ['MANAGE_ORDERS'] to Permission db objects."""
    permissions = get_permissions_enum_dict()
    return get_permissions([permissions[name].value for name in names])


def get_permission_names(permissions: Iterable["Permission"]):
    """Convert Permissions db objects to list of Permission enums."""
    permission_dict = get_permissions_enum_dict()
    names = set()
    for perm in permissions:
        for _, perm_enum in permission_dict.items():
            if perm.codename == perm_enum.codename:
                names.add(perm_enum.name)
    return names


def get_permissions_enum_list():
    permissions_list = [
        (enum.name, enum.value)
        for permission_enum in PERMISSIONS_ENUMS
        for enum in permission_enum
    ]
    return permissions_list


def get_permissions(permissions=None):
    if permissions is None:
        codenames = get_permissions_codename()
    else:
        codenames = split_permission_codename(permissions)
    return get_permissions_from_codenames(codenames)


def get_permissions_from_codenames(permission_codenames: List[str]):
    return (
        Permission.objects.filter(codename__in=permission_codenames)
        .prefetch_related("content_type")
        .order_by("codename")
    )
