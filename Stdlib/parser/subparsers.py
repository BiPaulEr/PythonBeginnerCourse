import argparse

# Sample database (dictionary) to store users
users = {}

# Create the argument parser
parser = argparse.ArgumentParser(description="Système de gestion des utilisateurs")
subparsers = parser.add_subparsers(dest='command', help='Commandes utilisateur')

# Add user command
add_parser = subparsers.add_parser('add', help='Ajouter un nouvel utilisateur')
add_parser.add_argument('name', help="Nom de l'utilisateur")

# Delete user command
delete_parser = subparsers.add_parser('delete', help='Supprimer un utilisateur existant')
delete_parser.add_argument('id', help="ID de l'utilisateur")

# Parse arguments
args = parser.parse_args()

# Handle commands
if args.command == 'add':
    user_id = len(users) + 1  # Simple way to generate a unique ID
    users[user_id] = args.name
    print(f"Utilisateur ajouté : ID={user_id}, Nom={args.name}")

elif args.command == 'delete':
    user_id = int(args.id)
    if user_id in users:
        deleted_name = users.pop(user_id)
        print(f"Utilisateur supprimé : ID={user_id}, Nom={deleted_name}")
    else:
        print(f"Erreur : Aucun utilisateur avec l'ID {user_id}")

else:
    parser.print_help()
