from multiprocessing import context
from django.shortcuts import render, redirect
from loja.models import Produto

def list_produto_view(request, id=None):
    produto = request.GET.get('produto')
    destaque = request.GET.get('destaque')
    promocao = request.GET.get('promocao')
    categoria = request.GET.get('categoria')
    fabricante = request.GET.get('fabricante')
    
    produtos = Produto.objects.all()
    
    if produto is not None:
        produtos = produtos.filter(Produto=produto)
    if promocao is not None:
        produtos = produtos.filter(promocao=promocao)
    if destaque is not None:
        produtos = produtos.filter(destaque=destaque)
    if categoria is not None:
        produtos = produtos.filter(categoria__Categoria=categoria)
    if fabricante is not None:
        produtos = produtos.filter(fabricante__Fabricante=fabricante)
    if id is not None:
        produtos = produtos.filter(id=id)

    context = {'produtos': produtos}

    return render(request, template_name='produto/produto.html', context=context, status=200)

def edit_produto_view(request, id=None):
    produtos = Produto.objects.all()

    if id is not None:
        produtos = produtos.filter(id=id)

    produto = produtos.first()
    context = {'produto': produto }

    return render(request, template_name='produto/produto-edit.html', context=context, status=200)

def edit_produto_postback(request, id=None):
    if request.method == 'POST':
        id = request.POST.get('id')
        produto = request.POST.get('Produto')
        destaque = request.POST.get('destaque')
        promocao = request.POST.get('promocao')
        msgPromocao = request.POST.get('msgPromocao')

        try:
            obj_produto = Produto.objects.filter(id=id).first()
            obj_produto.Produto = produto
            obj_produto.destaque = (destaque is not None)
            obj_produto.promocao = (promocao is not None)

            if msgPromocao is not None:
                obj_produto.msgPromocao = msgPromocao
            obj_produto.save()
            print("Produto %s salvo com sucesso" % produto)
        
        except Exception as e:
            print("Erro salvando edição de produto: %s" % e)
    
    return redirect("/produto")

def details_produto_view(request, id=None):
    produtos = Produto.objects.all()

    if id is not None:
        produtos = produtos.filter(id=id)

    produto = produtos.first()

    context = {'produto': produto}

    return render(request, template_name='produto/produto-details.html', context=context, status=200)

def delete_produto_view(request, id=None):
    produtos = Produto.objects.all()
    
    if id is not None:
        produtos = produtos.filter(id=id)

    produto = produtos.first()

    context = {'produto': produto}

    return render(request, template_name='produto/produto-delete.html', context=context, status=200)

def delete_produto_postback(request, id=None):
    if request.method == 'POST':
        id = request.POST.get('id')
        produto = request.POST.get("Produto")

        try:
            Produto.objects.filter(id=id).delete()
            print("Produto %s excluido com sucesso" % produto)
        except Exception as e:
            print("Erro salvando edição de produto: %s" % e)
        
    return redirect("/produto")

def create_produto_view(request, id=None):
    return render(request, template_name='produto/produto-create.html',status=200)