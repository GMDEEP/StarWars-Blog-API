"""empty message

Revision ID: 90fef6f0193b
Revises: ffe5dd75e629
Create Date: 2021-08-21 15:34:26.994999

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90fef6f0193b'
down_revision = 'ffe5dd75e629'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('people', sa.Column('birth_year', sa.String(length=250), nullable=False))
    op.add_column('people', sa.Column('eye_color', sa.String(length=250), nullable=False))
    op.add_column('people', sa.Column('gender', sa.String(length=250), nullable=False))
    op.add_column('people', sa.Column('hair_color', sa.String(length=250), nullable=False))
    op.add_column('people', sa.Column('height', sa.String(length=250), nullable=False))
    op.add_column('people', sa.Column('mass', sa.String(length=250), nullable=False))
    op.add_column('people', sa.Column('skin_color', sa.String(length=250), nullable=False))
    op.add_column('people', sa.Column('homeworld_id', sa.Integer(), nullable=True))
    op.add_column('people', sa.Column('url', sa.String(length=250), nullable=False))
    op.add_column('people', sa.Column('created', sa.String(length=250), nullable=False))
    op.add_column('people', sa.Column('edited', sa.String(length=250), nullable=False))
    op.create_unique_constraint(None, 'people', ['skin_color'])
    op.create_unique_constraint(None, 'people', ['eye_color'])
    op.create_unique_constraint(None, 'people', ['gender'])
    op.create_unique_constraint(None, 'people', ['url'])
    op.create_unique_constraint(None, 'people', ['hair_color'])
    op.create_unique_constraint(None, 'people', ['created'])
    op.create_unique_constraint(None, 'people', ['height'])
    op.create_unique_constraint(None, 'people', ['edited'])
    op.create_unique_constraint(None, 'people', ['mass'])
    op.create_unique_constraint(None, 'people', ['birth_year'])
    op.create_foreign_key(None, 'people', 'planet', ['homeworld_id'], ['id'])
    op.add_column('planet', sa.Column('diameter', sa.String(length=250), nullable=False))
    op.add_column('planet', sa.Column('rotation_period', sa.String(length=250), nullable=False))
    op.add_column('planet', sa.Column('orbital_period', sa.String(length=250), nullable=False))
    op.add_column('planet', sa.Column('gravity', sa.String(length=250), nullable=False))
    op.add_column('planet', sa.Column('population', sa.String(length=250), nullable=False))
    op.add_column('planet', sa.Column('climate', sa.String(length=250), nullable=False))
    op.add_column('planet', sa.Column('terrain', sa.String(length=250), nullable=False))
    op.add_column('planet', sa.Column('surface_water', sa.String(length=250), nullable=False))
    op.add_column('planet', sa.Column('url', sa.String(length=250), nullable=False))
    op.create_unique_constraint(None, 'planet', ['url'])
    op.create_unique_constraint(None, 'planet', ['population'])
    op.create_unique_constraint(None, 'planet', ['gravity'])
    op.create_unique_constraint(None, 'planet', ['climate'])
    op.create_unique_constraint(None, 'planet', ['diameter'])
    op.create_unique_constraint(None, 'planet', ['terrain'])
    op.create_unique_constraint(None, 'planet', ['rotation_period'])
    op.create_unique_constraint(None, 'planet', ['surface_water'])
    op.create_unique_constraint(None, 'planet', ['orbital_period'])
    op.add_column('vehicle', sa.Column('model', sa.String(length=250), nullable=False))
    op.add_column('vehicle', sa.Column('vehicle_class', sa.String(length=250), nullable=False))
    op.add_column('vehicle', sa.Column('manufacturer', sa.String(length=250), nullable=False))
    op.add_column('vehicle', sa.Column('length', sa.String(length=250), nullable=False))
    op.add_column('vehicle', sa.Column('cost_in_credits', sa.String(length=250), nullable=False))
    op.add_column('vehicle', sa.Column('crew', sa.String(length=250), nullable=False))
    op.add_column('vehicle', sa.Column('passengers', sa.String(length=250), nullable=False))
    op.add_column('vehicle', sa.Column('max_atmosphering_speed', sa.String(length=250), nullable=False))
    op.add_column('vehicle', sa.Column('cargo_capacity', sa.String(length=250), nullable=False))
    op.add_column('vehicle', sa.Column('consumables', sa.String(length=250), nullable=False))
    op.add_column('vehicle', sa.Column('url', sa.String(length=250), nullable=False))
    op.add_column('vehicle', sa.Column('created', sa.String(length=250), nullable=False))
    op.add_column('vehicle', sa.Column('edited', sa.String(length=250), nullable=False))
    op.create_unique_constraint(None, 'vehicle', ['created'])
    op.create_unique_constraint(None, 'vehicle', ['manufacturer'])
    op.create_unique_constraint(None, 'vehicle', ['edited'])
    op.create_unique_constraint(None, 'vehicle', ['max_atmosphering_speed'])
    op.create_unique_constraint(None, 'vehicle', ['url'])
    op.create_unique_constraint(None, 'vehicle', ['length'])
    op.create_unique_constraint(None, 'vehicle', ['cargo_capacity'])
    op.create_unique_constraint(None, 'vehicle', ['cost_in_credits'])
    op.create_unique_constraint(None, 'vehicle', ['consumables'])
    op.create_unique_constraint(None, 'vehicle', ['passengers'])
    op.create_unique_constraint(None, 'vehicle', ['crew'])
    op.create_unique_constraint(None, 'vehicle', ['model'])
    op.create_unique_constraint(None, 'vehicle', ['vehicle_class'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'vehicle', type_='unique')
    op.drop_constraint(None, 'vehicle', type_='unique')
    op.drop_constraint(None, 'vehicle', type_='unique')
    op.drop_constraint(None, 'vehicle', type_='unique')
    op.drop_constraint(None, 'vehicle', type_='unique')
    op.drop_constraint(None, 'vehicle', type_='unique')
    op.drop_constraint(None, 'vehicle', type_='unique')
    op.drop_constraint(None, 'vehicle', type_='unique')
    op.drop_constraint(None, 'vehicle', type_='unique')
    op.drop_constraint(None, 'vehicle', type_='unique')
    op.drop_constraint(None, 'vehicle', type_='unique')
    op.drop_constraint(None, 'vehicle', type_='unique')
    op.drop_constraint(None, 'vehicle', type_='unique')
    op.drop_column('vehicle', 'edited')
    op.drop_column('vehicle', 'created')
    op.drop_column('vehicle', 'url')
    op.drop_column('vehicle', 'consumables')
    op.drop_column('vehicle', 'cargo_capacity')
    op.drop_column('vehicle', 'max_atmosphering_speed')
    op.drop_column('vehicle', 'passengers')
    op.drop_column('vehicle', 'crew')
    op.drop_column('vehicle', 'cost_in_credits')
    op.drop_column('vehicle', 'length')
    op.drop_column('vehicle', 'manufacturer')
    op.drop_column('vehicle', 'vehicle_class')
    op.drop_column('vehicle', 'model')
    op.drop_constraint(None, 'planet', type_='unique')
    op.drop_constraint(None, 'planet', type_='unique')
    op.drop_constraint(None, 'planet', type_='unique')
    op.drop_constraint(None, 'planet', type_='unique')
    op.drop_constraint(None, 'planet', type_='unique')
    op.drop_constraint(None, 'planet', type_='unique')
    op.drop_constraint(None, 'planet', type_='unique')
    op.drop_constraint(None, 'planet', type_='unique')
    op.drop_constraint(None, 'planet', type_='unique')
    op.drop_column('planet', 'url')
    op.drop_column('planet', 'surface_water')
    op.drop_column('planet', 'terrain')
    op.drop_column('planet', 'climate')
    op.drop_column('planet', 'population')
    op.drop_column('planet', 'gravity')
    op.drop_column('planet', 'orbital_period')
    op.drop_column('planet', 'rotation_period')
    op.drop_column('planet', 'diameter')
    op.drop_constraint(None, 'people', type_='foreignkey')
    op.drop_constraint(None, 'people', type_='unique')
    op.drop_constraint(None, 'people', type_='unique')
    op.drop_constraint(None, 'people', type_='unique')
    op.drop_constraint(None, 'people', type_='unique')
    op.drop_constraint(None, 'people', type_='unique')
    op.drop_constraint(None, 'people', type_='unique')
    op.drop_constraint(None, 'people', type_='unique')
    op.drop_constraint(None, 'people', type_='unique')
    op.drop_constraint(None, 'people', type_='unique')
    op.drop_constraint(None, 'people', type_='unique')
    op.drop_column('people', 'edited')
    op.drop_column('people', 'created')
    op.drop_column('people', 'url')
    op.drop_column('people', 'homeworld_id')
    op.drop_column('people', 'skin_color')
    op.drop_column('people', 'mass')
    op.drop_column('people', 'height')
    op.drop_column('people', 'hair_color')
    op.drop_column('people', 'gender')
    op.drop_column('people', 'eye_color')
    op.drop_column('people', 'birth_year')
    # ### end Alembic commands ###
