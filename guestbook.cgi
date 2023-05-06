#!/bin/bash

horaDia=$(date "+%d/%m/%Y às %R")
path='/var/gopher/guestbook/guestbook.txt'
msg="$QUERY_STRING"

# Fazendo uma breve checagem para ver
# se podemos continuar.
if [[ ${#msg} -eq 0 ]]; then
	echo "É necessário digita uma mensagem."
	exit 1
elif [[ ${#msg} -ge "250" ]]; then
	echo "As mensagem podem conter até 250 caracteres."
	exit 1
fi


### Removendo a maioria dos caracteres que podem
# ser prejudiciais para o programa
re='[&*<>$()\`]+'
if [[ $msg =~ $re ]]; then
    echo "Contem caracteres não permitidos."
    exit 1
fi
re='(eval|rm|echo|cat|printf|\bmail)'
if [[ $msg =~ $re ]]; then
    echo "Não não. Aqui nois constroi fibra man."
    echo "Sua postagem obviamente não vai ser computada."
    exit 1
fi

# Copia de backup dos comentarios.
# maior que zero mete brasa.
#if [[ -s $path ]]; then
#    cp $path ${path}.bkp
#fi

# Quebrando após 67 caracteres em cada linha
msg=$(sed -e "s/.\{67\}/&\n/g" <<<$msg)

# Enviando para o Banco
echo "[$horaDia]" >> $path
echo "$msg" >> $path
echo "" >> $path
echo "" >> $path

cat <<'EOF'
        _________   _________
   ____/         \ /         \____
 /| ------------- |  ------------ |\
||| ------------- | ------------- |||
||| ------------- | ------------- |||
||| ------- ----- | ------------- |||
||| ------------- | ------------- |||
||| ------------- | ------------- |||
|||  ------------ | ----------    |||
||| ------------- |  ------------ |||
||| ------------- | ------------- |||
||| ------------- | ------ -----  |||
||| ------------  | ------------- |||
|||_____________  |  _____________|||
 /_____/--------\\_//--------\_____\

  Sua Foi Mensagem postada com sucesso!
  Para sua mensagem aparecer de um refresh na página anterior!

EOF
