import graphene
import api.schema
import users.shema


class Query(users.shema.Query, api.schema.Query, graphene.ObjectType):
    pass


class Mutation(users.shema.Mutation, api.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)