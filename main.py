from category import Category

def main():
    # Criando uma categoria
    print("Criando categoria...")
    category = Category(name="Eletrônicos", description="Produtos eletrônicos em geral")
    print(f"Categoria criada: {category.to_dict()}")
    print(f"Evento de criação: {category.events[0]}\n")

    # Atualizando a categoria
    print("Atualizando categoria...")
    category.update(name="Eletrônicos e Informática", description="Produtos eletrônicos e de informática")
    print(f"Categoria atualizada: {category.to_dict()}")
    print(f"Evento de atualização: {category.events[1]}\n")

    # Desativando a categoria
    print("Desativando categoria...")
    category.deactivate()
    print(f"Categoria desativada: {category.to_dict()}")
    print(f"Evento de desativação: {category.events[2]}\n")

    # Ativando a categoria
    print("Ativando categoria...")
    category.activate()
    print(f"Categoria ativada: {category.to_dict()}")
    print(f"Evento de ativação: {category.events[3]}\n")

    # Testando serialização
    print("Testando serialização...")
    category_dict = category.to_dict()
    print(f"Categoria serializada: {category_dict}")
    
    reconstructed_category = Category.from_dict(category_dict)
    print(f"Categoria reconstruída: {reconstructed_category.to_dict()}")
    
    # Verificando se são equivalentes
    print("\nVerificando equivalência...")
    print(f"IDs iguais: {category.id == reconstructed_category.id}")
    print(f"Nomes iguais: {category.name == reconstructed_category.name}")
    print(f"Descrições iguais: {category.description == reconstructed_category.description}")
    print(f"Status iguais: {category.is_active == reconstructed_category.is_active}")

if __name__ == "__main__":
    main()