function resolverEquacao() {
    const a = parseFloat(document.getElementById("entrada1").value);
    const b = parseFloat(document.getElementById("entrada2").value);
    const c = parseFloat(document.getElementById("entrada3").value);
    const doisa = 2 * a;
    const discriminante = b * b - 4 * a * c;
    let resultado;

    if (discriminante > 0) {
        let raiz1 = (-b + Math.sqrt(discriminante)) / doisa;
        let raiz2 = (-b - Math.sqrt(discriminante)) / doisa;
        resultado = `1° caso - Discriminante maior que zero:<br>
        <math>
            <mrow>
                <msub>
                <mi>X</mi>
                <mi>n</mi>
                </msub>
                <mo>=</mo>
                <msub>
                    <mi>C</mi>
                    <mn>1</mn>
                </msub>
                <mo>*</mo>
                <msup>
                    <mrow>
                        <mo>(</mo>
                        <mo>${raiz1.toFixed(2)}</mo>
                        <mo>)</mo>
                    </mrow>
                    <mi>n</mi>
                </msup>
                <mo>+</mo>
                <msub>
                    <mi>C</mi>
                    <mn>2</mn>
                </msub>
                <mo>*</mo>
                <msup>
                    <mrow>
                        <mo>(</mo>
                        <mo>${raiz2.toFixed(2)}</mo>
                        <mo>)</mo>
                    </mrow>
                    <mi>n</mi>
                </msup>
            </mrow>
            </math>`;
    } else if (discriminante < 0) {
        const parteReal = -b / (2 * a);
        const parteImaginaria = Math.sqrt(-discriminante) / (2 * a);
        let moduloP1 = parteReal * 2;
        moduloP1 = moduloP1.toFixed(2);
        let alpha = formatarAnguloNotavel(parteReal, parteImaginaria);
        resultado = `3° caso - Discriminante menor que zero:<br>
        <math>
            <msub>
                <mi>X</mi>
                <mi>n</mi>
            </msub>
            <mo>=</mo>
            <msup>
                <mrow>
                    <mo>|</mo>
                    <mi>${moduloP1}</mi>
                    <mo>|</mo>
                </mrow>
                <mi>n</mi>
            </msup>
            <mo>*</mo>
            <msub>
                <mi>K</mi>
                <mn>1</mn>
            </msub>
            <mo>*</mo>
            <mi>cos</mi>
            <mo>(</mo>
            <mrow>
                ${alpha}
            </mrow>
            <mi>n</mi>
            <mo>)</mo>
            <mo>+</mo>
            <msub>
                <mi>K</mi>
                <mn>2</mn>
            </msub>
            <mo>*</mo>
            <mi>sen</mi>
            <mo>(</mo>
            <mrow>
                ${alpha}
            </mrow>
            <mi>n</mi>
            <mo>)</mo>
        </math>`;
    } else {
        let raiz1 = (-b + Math.sqrt(discriminante)) / doisa;
        let raiz2 = (-b - Math.sqrt(discriminante)) / doisa;

        resultado = `2° caso - Discriminante igual a zero:<br>
        <math>
            <mrow>
                <msub>
                <mi>X</mi>
                <mi>n</mi>
                </msub>
                <mo>=</mo>
                <msub>
                    <mi>C</mi>
                    <mn>1</mn>
                </msub>
                <mo>*</mo>
                <msup>
                    <mrow>
                        <mo>(</mo>
                        <mo>${raiz1}</mo>
                        <mo>)</mo>
                    </mrow>
                    <mi>n</mi>
                </msup>
                <mo>+</mo>
                <msub>
                    <mi>C</mi>
                    <mn>2</mn>
                </msub>
                <mo>*</mo>
                <mi>n</mi>
                <mo>*</mo>
                <msup>
                    <mrow>
                        <mo>(</mo>
                        <mo>${raiz2}</mo>
                        <mo>)</mo>
                    </mrow>
                    <mi>n</mi>
                </msup>
            </mrow>
        </math>`;
    }

    document.getElementById("resultado").innerHTML = resultado;
}

// Função para exibir ângulos notáveis formatados como frações.
function formatarAnguloNotavel(parteReal, parteImaginaria) {
    let valor = (Math.atan(parteReal / parteImaginaria) * (180 / Math.PI)).toFixed(2);
    if (valor < 0) {
        valor = -valor;
    }

    
    
    
    

    if (valor >= 0 && valor < 15) { // 0
        return "<mn>0</mn>";
    } else if (valor >= 15 && valor <= 35) { // 30°
        return `<mfrac>
                    <mn>pi</mn>
                    <mn>6</mn>
                </mfrac>`;
    } else if (valor > 35 && valor <= 50) { // 45°
        return `<mfrac>
                    <mn>pi</mn>
                    <mn>4</mn>
                </mfrac>`;
    } else if (valor > 50 && valor <= 75) { // 60°
        return `<mfrac>
                    <mn>pi</mn>
                    <mn>3</mn>
                </mfrac>`;
    } else if (valor > 75  && valor <= 105) { // 90°
        return `<mfrac>
                    <mn>pi</mn>
                    <mn>2</mn>
                </mfrac>`;
    } else if (valor > 105 && valor < 127.5) { // 120°
        return `<mfrac>
                    <mn>2pi</mn>
                    <mn>3</mn>
                </mfrac>`;
    } else if (valor > 127.5 && valor <= 142.5) { // 135°
        return `<mfrac>
                    <mn>3pi</mn>
                    <mn>4</mn>
                </mfrac>`;
    } else if (valor > 142.5 && valor < 165) { // 150°
        return `<mfrac>
                    <mn>5pi</mn>
                    <mn>6</mn>
                </mfrac>`;
    } else if (valor > 165 && valor <= 195) { // 180°
        return "pi"
    } else if (valor > 195 && valor <= 225) { // 210° 
        return `<mfrac>
                    <mn>7pi</mn>
                    <mn>6</mn>
                </mfrac>`;
    } else if (valor > 225 && valor <= 232.5) { // 225°
        return `<mfrac>
                    <mn>5pi</mn>
                    <mn>4</mn>
                </mfrac>`;
    } else if (valor > 232.5 && valor <= 255) { // 240°
        return `<mfrac>
                    <mn>4pi</mn>
                    <mn>3</mn>
                </mfrac>`;
    } else if (valor > 255 && valor <= 285) { // 270°
        return `<mfrac>
                    <mn>3pi</mn>
                    <mn>2</mn>
                </mfrac>`;
    } else if (valor > 285 && valor <= 370.5) { // 300°
        return `<mfrac>
                    <mn>5pi</mn>
                    <mn>3</mn>
                </mfrac>`;
    } else if (valor > 370.5 && valor <= 322.5) { // 315°
        return `<mfrac>
                    <mn>7pi</mn>
                    <mn>4</mn>
                </mfrac>`;
    } else if (valor > 322.5 && valor <= 345) { // 330° 
        return `<mfrac>
                    <mn>11pi</mn>
                    <mn>6</mn>
                </mfrac>`;
    } else if (valor > 345 && valor <= 360) { // 360°
        return "<mn>2pi</mn>";
    }

    return valor;
}   