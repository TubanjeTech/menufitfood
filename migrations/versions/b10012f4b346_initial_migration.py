"""initial migration

Revision ID: b10012f4b346
Revises: 
Create Date: 2024-11-21 11:32:09.002275

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b10012f4b346'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account_name', sa.String(length=255), nullable=False),
    sa.Column('owner', sa.String(length=255), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('location', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('status', sa.String(length=255), nullable=False),
    sa.Column('last_login', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('admin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('type', sa.String(length=255), nullable=False),
    sa.Column('status', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('ingredients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('menu', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('image', sa.String(length=100), nullable=False),
    sa.Column('created_at', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('receipt_printer',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('restaurant_id', sa.Integer(), nullable=False),
    sa.Column('status', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('store_logs',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('restaurant_id', sa.Integer(), nullable=False),
    sa.Column('dish_id', sa.Integer(), nullable=False),
    sa.Column('store_field', sa.Text(), nullable=False),
    sa.Column('qty', sa.Integer(), nullable=False),
    sa.Column('requested', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account', sa.Integer(), nullable=False),
    sa.Column('category_name', sa.String(length=100), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['account'], ['account.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('category_name')
    )
    op.create_table('restaurants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account_id', sa.Integer(), nullable=False),
    sa.Column('rest_name', sa.String(length=100), nullable=False),
    sa.Column('menu_type', sa.Text(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.Column('logo', sa.String(length=200), nullable=False),
    sa.Column('country_of_res', sa.String(length=100), nullable=False),
    sa.Column('state_or_prov', sa.String(length=150), nullable=False),
    sa.Column('res_district', sa.String(length=150), nullable=False),
    sa.Column('visited', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['account_id'], ['account.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sales',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('account_id', sa.Integer(), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('item_name', sa.String(length=255), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('profit', sa.Float(), nullable=False),
    sa.Column('total_price', sa.Float(), nullable=False),
    sa.Column('staff', sa.String(length=255), nullable=False),
    sa.Column('status', sa.String(length=255), nullable=False),
    sa.Column('receipt', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['account.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account_id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=255), nullable=False),
    sa.Column('lastname', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('role', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['account.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('assistance',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('restaurant_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('status', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurants.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('departments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('restaurant_id', sa.Integer(), nullable=False),
    sa.Column('dep_name', sa.String(length=100), nullable=False),
    sa.Column('status', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurants.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('expences',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('restaurant_id', sa.Integer(), nullable=False),
    sa.Column('item_name', sa.Text(), nullable=False),
    sa.Column('stock_type', sa.Text(), nullable=False),
    sa.Column('qty_consumed', sa.Integer(), nullable=False),
    sa.Column('qty_instock', sa.Integer(), nullable=False),
    sa.Column('cost', sa.Float(), nullable=False),
    sa.Column('value', sa.Float(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurants.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('item_name', sa.String(length=255), nullable=False),
    sa.Column('img', sa.String(length=255), nullable=False),
    sa.Column('item_description', sa.Text(), nullable=False),
    sa.Column('qty', sa.Integer(), nullable=False),
    sa.Column('buying', sa.String(length=255), nullable=False),
    sa.Column('selling', sa.String(length=255), nullable=False),
    sa.Column('reorder', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['account'], ['account.id'], ),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('menu_categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('menu_categoryname', sa.String(length=100), nullable=False),
    sa.Column('icon', sa.String(length=30), nullable=False),
    sa.Column('visited', sa.Integer(), nullable=False),
    sa.Column('restaurant', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['restaurant'], ['restaurants.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('restaurant_details',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('restaurant_id', sa.Integer(), nullable=False),
    sa.Column('details', sa.Text(), nullable=False),
    sa.Column('logo', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('status', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurants.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('restaurant_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('restaurant_id', sa.Integer(), nullable=False),
    sa.Column('menu_type', sa.Text(), nullable=False),
    sa.Column('recorded_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurants.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('staff',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('restaurant_id', sa.Integer(), nullable=False),
    sa.Column('staff_name', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('staff_phone', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('status', sa.String(length=255), nullable=False),
    sa.Column('role', sa.String(length=255), nullable=False),
    sa.Column('pin', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurants.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dishes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('restaurant', sa.Integer(), nullable=False),
    sa.Column('dishes_name', sa.String(length=100), nullable=False),
    sa.Column('menu_categories_id', sa.Integer(), nullable=False),
    sa.Column('menu_option', sa.Enum('takeaway', 'room', 'direct_table', name='menu_options_enum'), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('cost', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=100), nullable=False),
    sa.Column('printer', sa.String(length=50), nullable=False),
    sa.Column('weight', sa.Float(), nullable=False),
    sa.Column('portion_size', sa.String(length=50), nullable=False),
    sa.Column('delivery_fee', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['menu_categories_id'], ['menu_categories.id'], ),
    sa.ForeignKeyConstraint(['restaurant'], ['restaurants.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('receipt',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('receipt_number', sa.Integer(), nullable=False),
    sa.Column('tableno', sa.Integer(), nullable=False),
    sa.Column('restaurant_id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('status', sa.Text(), nullable=False),
    sa.Column('cashier_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['cashier_id'], ['staff.id'], ),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurants.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('menues',
    sa.Column('id', sa.String(length=150), nullable=False),
    sa.Column('dishes_ref', sa.Integer(), nullable=False),
    sa.Column('contents', sa.Text(), nullable=False),
    sa.Column('warnings', sa.Text(), nullable=False),
    sa.Column('protein', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['dishes_ref'], ['dishes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('neworder',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dish', sa.String(length=255), nullable=False),
    sa.Column('restaurant', sa.Integer(), nullable=False),
    sa.Column('staff', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('status', sa.String(length=255), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('numberofpeople', sa.Integer(), nullable=False),
    sa.Column('tableno', sa.Text(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('preferences', sa.Text(), nullable=False),
    sa.Column('totalprice', sa.Integer(), nullable=False),
    sa.Column('phone', sa.Integer(), nullable=False),
    sa.Column('takeaway_counter', sa.Integer(), nullable=False),
    sa.Column('receipt', sa.Integer(), nullable=False),
    sa.Column('seen', sa.String(length=255), nullable=False),
    sa.Column('seen_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['receipt'], ['receipt.id'], ),
    sa.ForeignKeyConstraint(['restaurant'], ['restaurants.id'], ),
    sa.ForeignKeyConstraint(['staff'], ['staff.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('proforma',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('receipt', sa.Integer(), nullable=False),
    sa.Column('restaurant', sa.Integer(), nullable=False),
    sa.Column('tableno', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('status', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['receipt'], ['receipt.id'], ),
    sa.ForeignKeyConstraint(['restaurant'], ['restaurants.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('purchases',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('dish_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('supplier', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['dish_id'], ['dishes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('receipt_logs',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('staff_id', sa.Integer(), nullable=False),
    sa.Column('restaurant_id', sa.Integer(), nullable=False),
    sa.Column('receipt_id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('payment_mode', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['receipt_id'], ['receipt.id'], ),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurants.id'], ),
    sa.ForeignKeyConstraint(['staff_id'], ['staff.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('recipe',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('dish_id', sa.Integer(), nullable=False),
    sa.Column('ingredient_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('store', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['dish_id'], ['dishes.id'], ),
    sa.ForeignKeyConstraint(['ingredient_id'], ['ingredients.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stock',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('dish_id', sa.Integer(), nullable=False),
    sa.Column('main', sa.Integer(), nullable=False),
    sa.Column('main_qty', sa.Integer(), nullable=False),
    sa.Column('kitchen', sa.Integer(), nullable=False),
    sa.Column('kitchen_qty', sa.Integer(), nullable=False),
    sa.Column('bar', sa.Integer(), nullable=False),
    sa.Column('bar_qty', sa.Integer(), nullable=False),
    sa.Column('other1', sa.Integer(), nullable=False),
    sa.Column('other1_qty', sa.Integer(), nullable=False),
    sa.Column('other2', sa.Integer(), nullable=False),
    sa.Column('other2_qty', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['dish_id'], ['dishes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('menu_ordered', sa.String(length=50), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('tableno', sa.Integer(), nullable=False),
    sa.Column('ordered_by', sa.Integer(), nullable=False),
    sa.Column('restaurant', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=20), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['menu_ordered'], ['menues.id'], ),
    sa.ForeignKeyConstraint(['ordered_by'], ['staff.id'], ),
    sa.ForeignKeyConstraint(['restaurant'], ['restaurants.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('payment_mode',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('neworder_id', sa.Integer(), nullable=False),
    sa.Column('mode', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['neworder_id'], ['neworder.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('payment_mode')
    op.drop_table('orders')
    op.drop_table('stock')
    op.drop_table('recipe')
    op.drop_table('receipt_logs')
    op.drop_table('purchases')
    op.drop_table('proforma')
    op.drop_table('neworder')
    op.drop_table('menues')
    op.drop_table('receipt')
    op.drop_table('dishes')
    op.drop_table('staff')
    op.drop_table('restaurant_type')
    op.drop_table('restaurant_details')
    op.drop_table('menu_categories')
    op.drop_table('items')
    op.drop_table('expences')
    op.drop_table('departments')
    op.drop_table('assistance')
    op.drop_table('user')
    op.drop_table('sales')
    op.drop_table('restaurants')
    op.drop_table('categories')
    op.drop_table('store_logs')
    op.drop_table('receipt_printer')
    op.drop_table('ingredients')
    op.drop_table('admin')
    op.drop_table('account')
    # ### end Alembic commands ###