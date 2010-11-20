import QMTypes as q

class Term:
    def __init__(self):
        self.Ops = []
        self.Coef = 1
        self.State = None
    def AddOp(self, Oper):
        self.Ops.append(Oper)
    def SetCoef(self, Coef):
        self.Coef = self.Coef * Coef
    def SetState(self, State):
        self.State = State
    def Identifier(self):
        return str(self.Ops) + str(self.State)
    def ToExprList(self):
        result = []
        result.append(q.Number(str(self.Coef)))
        
        result.append(q.Operator("*"))
    def __add__(self, other):
        t = Term()
        t.Ops = self.Ops
        t.State = self.State
        t.Coef = self.Coef + other.Coef
        return t
    def __repr__(self):
        retStr = str(self.Coef)
        for op in self.Ops:
            retStr += str(op)
        if not self.State == None:
            retStr += str(self.State)

        return retStr

class Evaluator:
    @staticmethod
    def Evaluate(Expr): #Expr is of Expression type
        terms = dict()

        t = Term()
        for item in Expr.contents:
            if isinstance(item, q.Expression):
                pass
            elif isinstance(item, q.State):
                t.SetState(item)
            elif isinstance(item, q.Operator):
                t.AddOp(item)
            elif isinstance(item, q.Number):
                t.SetCoef(item.val)
            elif isinstance(item, q.Operation):
                if item.val == "+":
                    print t.Identifier()
                    if terms.has_key(t.Identifier()):
                        terms[t.Identifier()] += t
                    else:
                        terms[t.Identifier()] = t
                    t = Term()
                elif item.val == "-":
                    if terms.has_key(t.Identifier()):
                        terms[t.Identifier()] += t
                    else:
                        terms[t.Identifier()] = t
                    t = Term()
                    t.SetCoef(-1)
                
        if terms.has_key(t.Identifier()):
            terms[t.Identifier()] += t
        else:
            terms[t.Identifier()] = t

        result = q.Expression()
        for term in terms.keys():
            result.AddToExpr(terms[term].ToExprList())
        
        return Expr

if __name__ == '__main__':
    a = q.Expression()
    a.AddToExpr(q.Number(5))
    a.AddToExpr(q.Operation("*"))
    a.AddToExpr(q.Operator("B"))
    a.AddToExpr(q.Operation("*"))
    a.AddToExpr(q.Operator("A"))
    a.AddToExpr(q.Operation("*"))
    a.AddToExpr(q.State("ket", "b"))
    a.AddToExpr(q.Operation("+"))
    a.AddToExpr(q.Number(6)) 
    a.AddToExpr(q.Operation("*"))
    a.AddToExpr(q.Operator("A"))
    a.AddToExpr(q.Operation("*"))
    a.AddToExpr(q.Operator("B"))
    a.AddToExpr(q.Operation("*"))
    a.AddToExpr(q.State("ket", "b"))
    print a
    #res = Evaluator.Evaluate(a)
    #print res
