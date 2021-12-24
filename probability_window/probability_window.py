import tkinter as tk
from scipy import stats


normValueSigma = 0
normValueM = 0
normValueX = 0


geoValueX= 0
geoValueP= 0

pmfValueN = 0
pmfValueP = 0
pmfValueX = 0

cdfValueN = 0
cdfValueP = 0
cdfValueX = 0

lambdaPoss = 0
possionX = 0
class title:
    def __init__(self, root, font):
        topFrame = tk.Frame(root)
        topFrame.pack(side=tk.TOP, pady=40)
        label = tk.Label(topFrame, text="Probability", font=font + (40, "italic"), fg="#4b50b0", bg="#84e9d9")
        label.pack()


class pmfBtn:
    def __init__(self, frame, font,txtPmfN,txtPmfP,txtPmfX,labelPmf):
        self.txtPmfN = txtPmfN
        self.txtPmfP = txtPmfP
        self.txtPmfX = txtPmfX
        self.labelPmf = labelPmf
        button = tk.Button(frame, text='PMF', command=self.calculate, font=font + (20,), bg="#4b50b0",
                           fg="#efefef", width=10)
        button.pack(side=tk.LEFT, padx=10)

    def calculate(self):
        global pmfValueN
        global pmfValueP
        global labelPmf
        pmfValueN = self.txtPmfN.getParameter().get('1.0', 'end')
        pmfValueP = self.txtPmfP.getParameter().get('1.0', 'end')
        pmfValueX = self.txtPmfX.getParameter().get('1.0', 'end')
        try:
            pmfValueN = float(pmfValueN)
            pmfValueP = float(pmfValueP)
            pmfValueX = float(pmfValueX)
        except:
            tk.messagebox.showinfo(
                title='Error!',
                message="Invalid data please select valid data.. All values set to zero"
            )
            pmfValueN = 0
            pmfValueP = 0
            pmfValueX = 0

        X = stats.binom(pmfValueN, pmfValueP)  # Declare X to be a binomial random variable
        self.labelPmf.config(text = "PMF = "+str(X.pmf(pmfValueX)))



class pmfTextBoxN:
    def __init__(self, frame, font):
        label = tk.Label(frame, text="N", font=font + (16, "italic"), fg="#4b50b0", bg="#84e9d9")
        label.pack(side=tk.LEFT, padx=10)
        self.T = tk.Text(frame, height=2, width=15,font=font)
        self.T.pack(side=tk.LEFT, padx=10)

    def getParameter(self):
        return self.T
class pmfTextBoxP:
    def __init__(self, frame, font):
        label = tk.Label(frame, text="P", font=font + (16, "italic"), fg="#4b50b0", bg="#84e9d9")
        label.pack(side=tk.LEFT, padx=10)
        self.T = tk.Text(frame, height=2, width=15,font=font)
        self.T.pack(side=tk.LEFT, padx=10)
    def getParameter(self):
        return self.T
class pmfTextBoxX:
    def __init__(self, frame, font):
        label = tk.Label(frame, text="X", font=font + (16, "italic"), fg="#4b50b0", bg="#84e9d9")
        label.pack(side=tk.LEFT, padx=10)
        self.T = tk.Text(frame, height=2, width=15,font=font)
        self.T.pack(side=tk.LEFT, padx=10)
    def getParameter(self):
        return self.T



class cdfBtn:
    def __init__(self, frame, font,txtCdfN,txtCdfP,txtCdfX,labelCdf):
        self.txtCdfN = txtCdfN
        self.txtCdfP = txtCdfP
        self.txtCdfX = txtCdfX
        self.labelCdf = labelCdf
        button = tk.Button(frame, text='CDF', command=self.calculate, font=font + (20,), bg="#4b50b0",
                           fg="#efefef", width=10)
        button.pack(side=tk.LEFT, padx=10)

    def calculate(self):
        global cdfValueX
        global cdfValueP
        global cdfValueN
        cdfValueN = self.txtCdfN.getParameter().get('1.0', 'end')
        cdfValueP = self.txtCdfP.getParameter().get('1.0', 'end')
        cdfValueX = self.txtCdfX.getParameter().get('1.0', 'end')
        try:
            cdfValueX = float(cdfValueX)
            cdfValueP = float(cdfValueP)
            cdfValueN = float(cdfValueN)
        except:
            tk.messagebox.showinfo(
                title='Error!',
                message="Invalid data please select valid data.. All values set to zero"
            )
            cdfValueN = 0
            cdfValueP = 0
            cdfValueX = 0

        X = stats.binom(cdfValueN, cdfValueP)  # Declare X to be a binomial random variable
        self.labelCdf.config(text = "CDF = "+str(X.cdf(cdfValueX)))



class cdfTextBoxN:
    def __init__(self, frame, font):
        label = tk.Label(frame, text="N", font=font + (16, "italic"), fg="#4b50b0", bg="#84e9d9")
        label.pack(side=tk.LEFT, padx=10)
        self.T = tk.Text(frame, height=2, width=15,font=font)
        self.T.pack(side=tk.LEFT, padx=10)

    def getParameter(self):
        return self.T
class cdfTextBoxP:
    def __init__(self, frame, font):
        label = tk.Label(frame, text="P", font=font + (16, "italic"), fg="#4b50b0", bg="#84e9d9")
        label.pack(side=tk.LEFT, padx=10)
        self.T = tk.Text(frame, height=2, width=15,font=font)
        self.T.pack(side=tk.LEFT, padx=10)
    def getParameter(self):
        return self.T
class cdfTextBoxX:
    def __init__(self, frame, font):
        label = tk.Label(frame, text="X", font=font + (16, "italic"), fg="#4b50b0", bg="#84e9d9")
        label.pack(side=tk.LEFT, padx=10)
        self.T = tk.Text(frame, height=2, width=15,font=font)
        self.T.pack(side=tk.LEFT, padx=10)
    def getParameter(self):
        return self.T



class possionBtn:
    def __init__(self, frame, font,txtlambda,txtPossionX,labelpossion):
        self.txtlambda = txtlambda
        self.txtPossionX = txtPossionX
        self.labelCdf = labelpossion
        button = tk.Button(frame, text='poisson PMF', command=self.calculate, font=font + (20,), bg="#4b50b0",
                           fg="#efefef", width=10)
        button.pack(side=tk.LEFT, padx=10)

    def calculate(self):
        global lambdaPoss
        lambdaPoss = self.txtlambda.getParameter().get('1.0', 'end')
        possionX = self.txtPossionX.getParameter().get('1.0', 'end')
        try:
            lambdaPoss = float(lambdaPoss)
            possionX = float(possionX)
        except:
            tk.messagebox.showinfo(
                title='Error!',
                message="Invalid data please select valid data.. All values set to zero"
            )
            lambdaPoss = 0
            possionX = 0
            # print("Hello")
        X = stats.poisson(lambdaPoss)  # Declare X to be a binomial random variable
        self.labelCdf.config(text = "PMF = "+str(X.pmf(possionX)))



class lambdaPossion:
    def __init__(self, frame, font):
        label = tk.Label(frame, text="lambda ", font=font + (16, "italic"), fg="#4b50b0", bg="#84e9d9")
        label.pack(side=tk.LEFT, padx=10)
        self.T = tk.Text(frame, height=2, width=15,font=font)
        self.T.pack(side=tk.LEFT, padx=10)

    def getParameter(self):
        return self.T
class xPossion:
    def __init__(self, frame, font):
        label = tk.Label(frame, text="X ", font=font + (16, "italic"), fg="#4b50b0", bg="#84e9d9")
        label.pack(side=tk.LEFT, padx=10)
        self.T = tk.Text(frame, height=2, width=15,font=font)
        self.T.pack(side=tk.LEFT, padx=10)

    def getParameter(self):
        return self.T

#Geometric Random Variable
class geoBtn:
    def __init__(self, frame, font,txtGeoP,txtGeoX,labelGeo):
        self.txtGeoP=txtGeoP
        self.txtGeoX=txtGeoX
        self.labelGeo=labelGeo
        button = tk.Button(frame, text='Geometric', command=self.calculate, font=font + (20,), bg="#4b50b0",
                           fg="#efefef", width=10)
        button.pack(side=tk.LEFT, padx=10)

    def calculate(self):
        global geoValueX
        global geoValueP
        global labelGeo
        geoValueP = self.txtGeoP.getParameter().get('1.0', 'end')
        geoValueX = self.txtGeoX.getParameter().get('1.0', 'end')
        try:
            geoValueP = float(geoValueP)
            geoValueX = float(geoValueX)
        except:
            tk.messagebox.showinfo(
                title='Error!',
                message="Invalid data please select valid data.. All values set to zero"
            )
            geoValueP = 0
            geoValueX = 0
            # print("Hello")
        X = stats.geom(geoValueP)  # Declare X to be a binomial random variable
        self.labelGeo.config(text = "Geo = "+str(X.pmf(geoValueX)))

#textbox for Geo Rv
class GeoTextBoxX:
    def __init__(self, frame, font):
        label = tk.Label(frame, text="X", font=font + (16, "italic"), fg="#4b50b0", bg="#84e9d9")
        label.pack(side=tk.LEFT, padx=10)
        self.T = tk.Text(frame, height=2, width=15,font=font)
        self.T.pack(side=tk.LEFT, padx=10)

    def getParameter(self):
        return self.T

class GeoTextBoxP:
    def __init__(self, frame, font):
        label = tk.Label(frame, text="P", font=font + (16, "italic"), fg="#4b50b0", bg="#84e9d9")
        label.pack(side=tk.LEFT, padx=10)
        self.T = tk.Text(frame, height=2, width=15,font=font)
        self.T.pack(side=tk.LEFT, padx=10)

    def getParameter(self):
        return self.T


# Normal dist
class normalBtn:
    def __init__(self, frame, font,txtNormalSigma,txtNormalM,txtNormalX,labelNormal):
        self.txtNormalSigma=txtNormalSigma
        self.txtNormalM=txtNormalM
        self.txtNormalX=txtNormalX
        self.labelNormal = labelNormal
        button = tk.Button(frame, text='Normal', command=self.calculate, font=font + (20,), bg="#4b50b0",
                           fg="#efefef", width=10)
        button.pack(side=tk.LEFT, padx=10)

    def calculate(self):
        global normValueSigma
        global normValueM
        global normValueX
        global labelNormal
        normValueM = self.txtNormalM.getParameter().get('1.0', 'end')
        normValueX = self.txtNormalX.getParameter().get('1.0', 'end')
        normValueSigma = self.txtNormalSigma.getParameter().get('1.0', 'end')
        try:
            normValueM = float(normValueM)
            normValueX = float(normValueX)
            normValueSigma = float(normValueSigma)
        except:
            tk.messagebox.showinfo(
                title='Error!',
                message="Invalid data please select valid data.. All values set to zero"
            )
            normValueM = 0
            normValueX = 0
            normValueSigma = 0
        X = stats.norm(normValueM,normValueSigma)  # Declare X to be a Normal random variable
        self.labelNormal.config(text = "Normal PDF = "+str(X.pdf(normValueX)))

#textbox for Normal Dist
class txtNormalX:
    def __init__(self, frame, font):
        label = tk.Label(frame, text="X", font=font + (16, "italic"), fg="#4b50b0", bg="#84e9d9")
        label.pack(side=tk.LEFT, padx=10)
        self.T = tk.Text(frame, height=2, width=15,font=font)
        self.T.pack(side=tk.LEFT, padx=10)

    def getParameter(self):
        return self.T

class txtNormalM:
    def __init__(self, frame, font):
        label = tk.Label(frame, text="Mean", font=font + (16, "italic"), fg="#4b50b0", bg="#84e9d9")
        label.pack(side=tk.LEFT, padx=10)
        self.T = tk.Text(frame, height=2, width=15,font=font)
        self.T.pack(side=tk.LEFT, padx=10)

    def getParameter(self):
        return self.T

class txtNormalSigma:
    def __init__(self, frame, font):
        label = tk.Label(frame, text="Standard Deviation", font=font + (16, "italic"), fg="#4b50b0", bg="#84e9d9")
        label.pack(side=tk.LEFT, padx=10)
        self.T = tk.Text(frame, height=2, width=15,font=font)
        self.T.pack(side=tk.LEFT, padx=10)

    def getParameter(self):
        return self.T



def run(dataFrame):
    root = tk.Tk()
    root.title("Probability")
    root.config(bg="#84e9d9")
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))
    root.state('zoomed')
    font = ("Helvetica",)
    root.option_add('*TCombobox*Listbox.font', font + (15,))

    # title of window
    title(root, font)



    framePmf = tk.Frame(root, bg="#84e9d9")
    framePmf.pack(padx = 20,pady=30)
    txtPmfN = pmfTextBoxN(framePmf, font)
    txtPmfP = pmfTextBoxP(framePmf, font)
    txtPmfX = pmfTextBoxX(framePmf, font)
    labelPmf = tk.Label(framePmf, text="Binomial PMF = ", font=font + (16, "italic"), fg="#4b50b0", bg="#84e9d9")
    pmfBtn(framePmf, font,txtPmfN,txtPmfP,txtPmfX,labelPmf)
    labelPmf.pack(side=tk.LEFT, padx=10)


    frameCdf = tk.Frame(root, bg="#84e9d9")
    frameCdf.pack(padx = 20,pady=30)
    txtCdfN = cdfTextBoxN(frameCdf, font)
    txtCdfP = cdfTextBoxP(frameCdf, font)
    txtCdfX = cdfTextBoxX(frameCdf, font)
    labelCdf = tk.Label(frameCdf, text="Binomial CDF = ", font=font + (16, "italic"), fg="#4b50b0", bg="#84e9d9")
    cdfBtn(frameCdf, font,txtCdfN,txtCdfP,txtCdfX,labelCdf)
    labelCdf.pack(side=tk.LEFT, padx=10)



    framePossion = tk.Frame(root, bg="#84e9d9")
    framePossion.pack(padx = 20,pady=30)
    txtlambda = lambdaPossion(framePossion, font)
    txtPossionX = xPossion(framePossion, font)
    labelPossion = tk.Label(framePossion, text="Possion PMF = ", font=font + (16, "italic"), fg="#4b50b0", bg="#84e9d9")
    possionBtn(framePossion, font,txtlambda,txtPossionX,labelPossion)
    labelPossion.pack(side=tk.LEFT, padx=10)

    #geo btn
    frameGeometric = tk.Frame(root, bg="#84e9d9")
    frameGeometric.pack(padx = 20,pady=30)
    txtgeoP = GeoTextBoxP(frameGeometric, font)
    txtgeoX = GeoTextBoxX(frameGeometric, font)
    labelGeo = tk.Label(frameGeometric, text="Geometric PMF = ", font=font + (16, "italic"), fg="#4b50b0", bg="#84e9d9")
    geoBtn(frameGeometric, font,txtgeoP,txtgeoX,labelGeo)
    labelGeo.pack(side=tk.LEFT, padx=10)

    #normal btn
    frameNormal = tk.Frame(root, bg="#84e9d9")
    frameNormal.pack(padx = 20,pady=30)
    txtNormalSigmaa = txtNormalSigma(frameNormal, font)
    txtNormX = txtNormalX(frameNormal, font)
    txtNormM = txtNormalM(frameNormal, font)
    labelNormal = tk.Label(frameNormal, text="Normal PDF = ", font=font + (16, "italic"), fg="#4b50b0", bg="#84e9d9")
    normalBtn(frameNormal, font,txtNormalSigmaa,txtNormM,txtNormX,labelNormal)
    labelNormal.pack(side=tk.LEFT, padx=10)

    root.mainloop()
