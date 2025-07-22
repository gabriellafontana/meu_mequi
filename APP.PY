import random

#cardapio com os lanches mais comuns
burgers = [ 'Big Mac', 'Cheddar McMelt', 'Quarterão com Queijo', 'McChicken', 
    'Duplo Cheeseburger', 'McFish', 'McVeggie', 'Duplo Barbecue Bacon',
    'Big Tasty', 'McNífico Bacon']

sides = [ 'McFritas Pequena', 'McFritas Média', 'McFritas Grande',
    'Onion Rings', 'Chicken McNuggets (6)', 'Chicken McNuggets (10)',
    'Tomatinho', 'Salada']

drinks = ['Coca-Cola', 'Coca-Cola Zero', 'Guaraná', 'Guaraná Zero',
    'Suco de Laranja', 'Suco de Maçã', 'Água Mineral', 'Água com Gás']

desserts = [ 'McFlurry Oreo', 'McFlurry KitKat', 'Casquinha de Baunilha',
    'Sundae de Chocolate', 'Sundae de Morango', 'Torta de Maçã']

sauces = ['Barbecue', 'Agridoce', 'Maionese Especial', 'Ketchup', 'Mostarda']

#gerador aleatorio de pedidos

def gerar_pedido():
    selected_burger = random.choice(burgers)
    selected_side= random.choice(sides)
    selected_drink = random.choice(drinks)
    selected_dessert = random.choice(desserts)
    selected_sauce= random.choice(sauces)

    print("\n Pedido Gerado:")
    print(f"Sanduiche: {selected_burger}")
    print(f"Acompanhamento: {selected_side}")
    print(f"Bebida: {selected_drink}")
    print(f"Molho: {selected_sauce}\n")

if __name__ =="__main__":
    print("Bem vindo ao gerador de pedidos aleatorio daquele restaurante famoso :)")
    input("Pressione Entre para gerar um pedido...\n")
    gerar_pedido()