import os
from dotenv import load_dotenv
import nextcord
from nextcord.ext import commands


client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    activity = nextcord.Game(name='Chame o suporte direto no PV com !ajuda')
    await client.change_presence(activity=activity)
    print(f'Bot {client.user.name} conectado')


class Botoes(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None
    # BOTOES DO DEPARTAMENTO

    @nextcord.ui.button(label='1 - Central de Vendas / OPS', style=nextcord.ButtonStyle.green, custom_id='btn1')
    async def departamento1(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message('A opção 1 foi selecionada')
        self.value = 'btn1'
        self.stop()

    @nextcord.ui.button(label='2 - Qualidade', style=nextcord.ButtonStyle.green, custom_id='btn2')
    async def departamento2(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message('A opção 2 foi selecionada')
        self.value = 'btn1'
        self.stop()

    @nextcord.ui.button(label='3 - Treinamento', style=nextcord.ButtonStyle.green, custom_id='btn3')
    async def departamento3(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message('A opção 3 foi selecionada')
        self.value = 'btn1'
        self.stop()

    @nextcord.ui.button(label='4 - Backoffice/CS', style=nextcord.ButtonStyle.green, custom_id='btn4')
    async def departamento4(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message('A opção 4 selecionada')
        self.value = 'btn1'
        self.stop()


class botaoes_op(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    # BOTOES DO OPERACAO
    @nextcord.ui.button(label='1- Claro', style=nextcord.ButtonStyle.green, custom_id='bt1')
    async def operacao1(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message('A opção op 1 foi selecionada')
        self.value = True
        self.stop()

    @nextcord.ui.button(label='2- Vivo', style=nextcord.ButtonStyle.green, custom_id='bt2')
    async def operacao2(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message('A opção op 2 foi selecionada')
        self.value = True
        self.stop()

    @nextcord.ui.button(label='3- PDP', style=nextcord.ButtonStyle.green, custom_id='bt3')
    async def operacao3(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message('A opção op 3 foi selecionada')
        self.value = True
        self.stop()

    @nextcord.ui.button(label='4- Multimarcas', style=nextcord.ButtonStyle.green, custom_id='bt4')
    async def operacao4(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message('A opção op 4 foi selecionada')
        self.value = True
        self.stop()

    @nextcord.ui.button(label='5- Health', style=nextcord.ButtonStyle.green, custom_id='bt5')
    async def operacao5(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message('A opção op 5 foi selecionada')
        self.value = True
        self.stop()

    @nextcord.ui.button(label='6- Itau', style=nextcord.ButtonStyle.green, custom_id='bt6')
    async def operacao6(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message('A opção op 6 foi selecionada')
        self.value = True
        self.stop()

    @nextcord.ui.button(label='7- Rodobens', style=nextcord.ButtonStyle.green, custom_id='bt7')
    async def operacao7(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message('A opção op 7 foi selecionada')
        self.value = True
        self.stop()


class botoes_motivo(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    # BOTOES DO MOTIVO
    @nextcord.ui.button(label='1- Estou com um Problema', style=nextcord.ButtonStyle.green, custom_id='bt1')
    async def motivo1(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message('A opção 1 foi selecionada')
        self.value = 'bt1'
        self.stop()

    @nextcord.ui.button(label='2- Preciso realizar uma Solicitação', style=nextcord.ButtonStyle.green, custom_id='bt2')
    async def motivo2(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message('A opção 2 foi selecionada')
        self.value = 'bt2'
        self.stop()

    @nextcord.ui.button(label='3- Tenho uma Dúvida', style=nextcord.ButtonStyle.green, custom_id='bt3')
    async def motivo3(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message('A opção 3 foi selecionada')
        self.value = 'bt3'
        self.stop()

    @nextcord.ui.button(label='4- Outros', style=nextcord.ButtonStyle.green, custom_id='bt4')
    async def motivo4(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message('A opção 4 selecionada')
        self.value = 'bt4'
        self.stop()


class botoes_problema(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    # BOTOES DO PROBLEMA
    @nextcord.ui.button(label='1- Problemas com Phone Manager', style=nextcord.ButtonStyle.green, custom_id='pbt1')
    async def problema1(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message('A opção op 1 foi selecionada')
        self.value = True
        self.stop()

    @nextcord.ui.button(label='2- Problemas no Infrasip', style=nextcord.ButtonStyle.green, custom_id='pbt2')
    async def problema2(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message('A opção op 2 foi selecionada')
        self.value = True
        self.stop()

    @nextcord.ui.button(label='3- Problemas com VPN', style=nextcord.ButtonStyle.green, custom_id='pbt3')
    async def problema3(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message('A opção op 3 foi selecionada')
        self.value = True
        self.stop()

    @nextcord.ui.button(label='4- Página de login da operadora não carrega', style=nextcord.ButtonStyle.green, custom_id='pbt4')
    async def problema4(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message('A opção op 4 foi selecionada')
        self.value = True
        self.stop()

    @nextcord.ui.button(label='5- Hubspot não realiza chamadas', style=nextcord.ButtonStyle.green, custom_id='pbt5')
    async def problema5(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message('A opção op 5 foi selecionada')
        self.value = True
        self.stop()

    @nextcord.ui.button(label='6- Problemas com equipamento/periféricos', style=nextcord.ButtonStyle.green, custom_id='pbt6')
    async def problema6(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message('A opção op 6 foi selecionada')
        self.value = True
        self.stop()

    @nextcord.ui.button(label='7- Não consegue logar no Windows', style=nextcord.ButtonStyle.green, custom_id='pbt7')
    async def problema7(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message('A opção op 7 foi selecionada')
        self.value = True
        self.stop()

    @nextcord.ui.button(label='8- Outras situações', style=nextcord.ButtonStyle.green, custom_id='pbt8')
    async def problema8(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message('A opção op 7 foi selecionada')
        self.value = True
        self.stop()


# BOTOES DO SOLICITACAO
'''class botoes_solicita(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None
    

    @nextcord.ui.button(label='SIM', style=nextcord.ButtonStyle.green, custom_id='btn1')
    async def solicitacao1(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message('A opção SIM foi selecionada')
        self.value = 'btn1'
        self.stop()

    @nextcord.ui.button(label='NAO', style=nextcord.ButtonStyle.red, custom_id='btn2')
    async def solicitacao2(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message('A opção NAO foi selecionada')
        self.value = True
        self.stop()'''


@client.command()
async def ajuda(ctx):

    view = Botoes()  # BOTOES DO DEPARTAMENTO
    view2 = botaoes_op()  # BOTOES DO OPERACAO
    view3 = botoes_motivo()  # BOTOES DO MOTIVO
    view4 = botoes_problema()  # BOTOES DO PROBLEMA
    # view5 = botoes_solicita()  # BOTOES DO SOLICITACAO

    await ctx.send(f'Olá, Tudo bem? Eu sou {client.user.name}, assistente virtual da Escale🤗')
    await ctx.send(
        'Para encaminhar a um atendente, primeiro vou precisar de algumas informações.\nPode me informar o seu departamento?',
        view=view)
    # VIEW DO DEPARTAMENTO
    await view.wait()
    if view.value is None:
        return
    if view.value == 'btn1':
        await ctx.send('Ótimo! Agora me diz qual a sua bandeira:', view=view2)
    # VIEW DO OPERACAO
    await view2.wait()
    if view2.value:
        await ctx.send('Qual o motivo pelo qual entrou em contato com o suporte?', view=view3)
    # VIEW DO MOTIVO
    await view3.wait()
    if view3.value == 'bt1':
        await ctx.send('Poderia me informar qual o problema está apresentando?', view=view4)

    if view3.value == 'bt2':
        await ctx.send('Muito bem!\nIrei passar para um dos nossos analistas!\nNormalmente nossa equipe responde em menos de 5 min, e conseguimos resolver\n'
                       'qualquer problema em até 25min. Porém, nos horários de pico das 09:00 às 10:30 e das\n14:00 às 15:30 o tempo de espera pode aumentar por conta do grande fluxo de\n'
                       'acionamentos causado pela troca de turnos.')

    if view3.value == 'bt3':
        await ctx.send('Muito bem!\nIrei passar para um dos nossos analistas!\nNormalmente nossa equipe responde em menos de 5 min, e conseguimos resolver\n'
                       'qualquer problema em até 25min. Porém, nos horários de pico das 09:00 às 10:30 e das\n14:00 às 15:30 o tempo de espera pode aumentar por conta do grande fluxo de\n'
                       'acionamentos causado pela troca de turnos.')
    if view3.value == 'bt4':
        await ctx.send(
            'Muito bem!\nIrei passar para um dos nossos analistas!\nNormalmente nossa equipe responde em menos de 5 min, e conseguimos resolver\n'
            'qualquer problema em até 25min. Porém, nos horários de pico das 09:00 às 10:30 e das\n14:00 às 15:30 o tempo de espera pode aumentar por conta do grande fluxo de\n'
            'acionamentos causado pela troca de turnos.')

    # VIEW DO PROBLEMA
    await view4.wait()
    if view4.value:
        await ctx.send(
            'Muito bem!\nIrei passar para um dos nossos analistas!\nNormalmente nossa equipe responde em menos de 5 min, e conseguimos resolver\n'
            'qualquer problema em até 25min. Porém, nos horários de pico das 09:00 às 10:30 e das\n14:00 às 15:30 o tempo de espera pode aumentar por conta do grande fluxo de\n'
            'acionamentos causado pela troca de turnos.')


load_dotenv()
TOKEN = os.getenv('TOKEN')
client.run(TOKEN)
