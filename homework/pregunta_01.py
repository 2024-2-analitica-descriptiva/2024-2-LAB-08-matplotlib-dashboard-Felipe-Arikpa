# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""


def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """

    import os
    import pandas as pd
    import matplotlib.pyplot as plt

    output_directory = 'docs'
    os.makedirs(output_directory, exist_ok=True)

    dataset = pd.read_csv('files/input/shipping-data.csv', sep=',')

    warehouse_block_count = dataset['Warehouse_block'].value_counts()
    mode_of_shipment_count = dataset['Mode_of_Shipment'].value_counts()
    average_customer_rating = dataset.groupby('Mode_of_Shipment')['Customer_rating'].describe()
    average_customer_rating = average_customer_rating[['mean', 'min', 'max']]
    weight_distribution = dataset['Weight_in_gms']



    def bar_graphic(datos):

        fig, ax = plt.subplots()

        for warehouse_block, count in datos.items():
            ax.bar(
            warehouse_block,
            count,
            color='tab:blue'
            )

            ax.text(
                x=warehouse_block,
                y=count - 300,
                s=str(count),
                ha='center',
                va='bottom',
                fontsize=14,
                color='white'
            )

        ax.set_title('Shipping per Warehouse', fontsize=17)
        ax.set_xlabel('Warehouse block', fontsize=9)

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['bottom'].set_color('darkgrey')
        ax.get_yaxis().set_visible(False)

        path_bar = os.path.join(output_directory, 'shipping_per_warehouse.png')
        plt.savefig(path_bar)



    def pie_graphic(datos):

        fig, ax = plt.subplots()

        colors =['tab:blue', 'navy', 'tab:cyan',]

        wedges, texts, autotexts = ax.pie(
                x=datos,
                labels=datos.index,
                wedgeprops={'width':0.4},
                colors=colors,
                autopct='%1.2f%%',
                startangle=90,
                pctdistance=0.8,
        )

        ax.set_title('Mode of shipment', fontsize=17)

        for autotext in autotexts:
            autotext.set_fontsize(10)
            autotext.set_color('white')

        for text, color in zip(texts, colors):
            text.set_fontsize(12)
            text.set_color(color)

        path_pie = os.path.join(output_directory, 'mode_of_shipment.png')
        plt.savefig(path_pie)
    


    def barh_graphic(datos):

        fig, ax = plt.subplots()

        ax.barh(
            y=datos.index.values,
            width=datos['max'].values -1,
            left=datos['min'].values,
            height=0.9,
            color='gainsboro',
            alpha=0.4
        )

        colors = ['tab:green' if value >= 3 else 'tab:red' for value in average_customer_rating['mean'].values]

        ax.barh(
            y=datos.index.values,
            width=datos['mean'].values -1,
            left=datos['min'].values,
            color=colors,
            height=0.5,
            alpha=1
        )

        ax.set_title('Average Customer Rating', fontsize=17)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color('darkgrey')
        ax.spines['bottom'].set_color('darkgrey')

        path_barh = os.path.join(output_directory, 'average_customer_rating.png')
        plt.savefig(path_barh)



    def hist_graphic(datos):

        fig, ax = plt.subplots()

        ax.hist(
            x=datos,
            color='tab:cyan',
            edgecolor='mediumturquoise'
        )

        ax.set_title('Shipped Weight Distribution', fontsize=17)

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color('darkgrey')
        ax.spines['bottom'].set_color('darkgrey')

        path_hist = os.path.join(output_directory, 'weight_distribution.png')
        plt.savefig(path_hist)


    def create_html_path(output_directory):

        path_html = os.path.join(output_directory, 'index.html')

        with open(path_html, 'w') as file:
            file.write(
                """
        <!DOCTYPE html>
        <html>
            <body>
                <h1>Shipping Dashboard Example</h1>
                <div style="width:45%;float:left">
                    <img src="shipping_per_warehouse.png" alt="Fig 1">
                    <img src="mode_of_shipment.png" alt="Fig 2">
                </div>
                <div style="width:45%;float:left">
                    <img src="average_customer_rating.png" alt="Fig 3">
                    <img src="weight_distribution.png" alt="Fig 4">
                </div>
            </body>
        </html>
        """
            )


    bar_graphic(datos=warehouse_block_count)
    pie_graphic(datos=mode_of_shipment_count)
    barh_graphic(datos=average_customer_rating)
    hist_graphic(datos=weight_distribution)
    create_html_path(output_directory=output_directory)

    return print('dashboard creado exitosamente')


pregunta_01()





