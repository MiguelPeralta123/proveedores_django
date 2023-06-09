from django import forms
from .models import Proveedor
from .options import *

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['empresa', 'codigo', 'tipo_alta', 'contribuyente', 'razon_social', 'rfc', 'curp', 'regimen_capital', 'nombre_fiscal', 'nombre_comercial', 'regimen_fiscal', 'uso_cdfi', 'representante_legal', 'telefono_1', 'telefono_2', 'contacto', 'grupo', 'correo_general', 'correo_pagos', 'sitio_web', 'rubro', 'tipo_operacion', 'tipo_tercero', 'id_fiscal', 'agente_aduanal', 'reg_inc_fiscal', 'impuesto_cedular', 'venc_s_fecha', 'dias_para_entrega_completa', 'limite_credito_MN', 'limite_credito_ME', 'dias_credito', 'monto_credito', 'retencion_iva', 'retencion_isr', 'iva_frontera', 'codigo_postal', 'pais', 'estado', 'ciudad', 'municipio', 'localidad', 'colonia', 'calle', 'numero_exterior', 'numero_interior', 'banco', 'cuenta', 'moneda', 'clabe', 'banco_2', 'cuenta_2', 'moneda_2', 'clabe_2', 'usar_en_portal_proveedores', 'no_aplica_para_rafaga', 'no_relacionar_OC', 'constancia_situacion_fiscal', 'estado_cuenta_bancario']
        widgets = {
            'empresa': forms.Select(choices=EMPRESA_LIST, attrs={'class':'form-control', 'initial':''}),
            'codigo': forms.TextInput(attrs={'class':'form-control'}),
            'tipo_alta': forms.Select(choices=TIPO_ALTA_LIST, attrs={'class':'form-control', 'initial':''}),
            'contribuyente': forms.Select(choices=CONTRIBUYENTE_LIST, attrs={'class':'form-control', 'initial':''}),
            'razon_social': forms.TextInput(attrs={'class':'form-control'}),
            'rfc': forms.TextInput(attrs={'class':'form-control'}),
            'curp': forms.TextInput(attrs={'class':'form-control'}),
            'regimen_capital': forms.Select(choices=REGIMEN_CAPITAL_LIST, attrs={'class':'form-control', 'initial':''}),
            'nombre_fiscal': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_comercial': forms.TextInput(attrs={'class':'form-control'}),
            'regimen_fiscal': forms.Select(choices=REGIMEN_FISCAL_LIST, attrs={'class':'form-control', 'initial':''}),
            'uso_cdfi': forms.Select(choices=USO_CFDI_LIST, attrs={'class':'form-control', 'initial':''}),
            'representante_legal': forms.TextInput(attrs={'class':'form-control'}),
            'telefono_1': forms.TextInput(attrs={'class':'form-control'}),
            'telefono_2': forms.TextInput(attrs={'class':'form-control'}),
            'contacto': forms.TextInput(attrs={'class':'form-control'}),
            'grupo': forms.TextInput(attrs={'class':'form-control'}),
            'correo_general': forms.TextInput(attrs={'class':'form-control'}),
            'correo_pagos': forms.TextInput(attrs={'class':'form-control'}),
            'sitio_web': forms.TextInput(attrs={'class':'form-control'}),
            'rubro': forms.Select(choices=RUBRO_LIST, attrs={'class':'form-control', 'initial':''}),
            'tipo_operacion': forms.Select(choices=TIPO_OPERACION_LIST, attrs={'class':'form-control', 'initial':''}),
            'tipo_tercero': forms.Select(choices=TIPO_TERCERO_LIST, attrs={'class':'form-control', 'initial':''}),
            'id_fiscal': forms.TextInput(attrs={'class':'form-control'}),
            'agente_aduanal': forms.TextInput(attrs={'class':'form-control'}),
            'reg_inc_fiscal': forms.TextInput(attrs={'class':'form-control'}),
            'impuesto_cedular': forms.TextInput(attrs={'class':'form-control'}),
            'venc_s_fecha': forms.DateInput(attrs={'type':'date'}),
            'dias_para_entrega_completa': forms.TextInput(attrs={'class':'form-control'}),
            'limite_credito_MN': forms.TextInput(attrs={'class':'form-control'}),
            'limite_credito_ME': forms.TextInput(attrs={'class':'form-control'}),
            'dias_credito': forms.TextInput(attrs={'class':'form-control'}),
            'monto_credito': forms.TextInput(attrs={'class':'form-control'}),
            'retencion_iva': forms.Select(choices=RETENCION_IVA_LIST, attrs={'class':'form-control', 'initial':''}),
            'retencion_isr': forms.Select(choices=RETENCION_ISR_LIST, attrs={'class':'form-control', 'initial':''}),
            'iva_frontera': forms.Select(choices=IVA_FRONTERA_LIST, attrs={'class':'form-control', 'initial':''}),
            'codigo_postal': forms.TextInput(attrs={'class':'form-control'}),
            'pais': forms.TextInput(attrs={'class':'form-control'}),
            'estado': forms.TextInput(attrs={'class':'form-control'}),
            'ciudad': forms.TextInput(attrs={'class':'form-control'}),
            'municipio': forms.TextInput(attrs={'class':'form-control'}),
            'localidad': forms.TextInput(attrs={'class':'form-control'}),
            'colonia': forms.TextInput(attrs={'class':'form-control'}),
            'calle': forms.TextInput(attrs={'class':'form-control'}),
            'numero_exterior': forms.TextInput(attrs={'class':'form-control'}),
            'numero_interior': forms.TextInput(attrs={'class':'form-control'}),
            'banco': forms.Select(choices=BANCO_LIST, attrs={'class':'form-control', 'initial':''}),
            'cuenta': forms.TextInput(attrs={'class':'form-control'}),
            'moneda': forms.Select(choices=MONEDA_LIST, attrs={'class':'form-control', 'initial':''}),
            'clabe': forms.TextInput(attrs={'class':'form-control'}),
            'banco_2': forms.Select(choices=BANCO_LIST, attrs={'class':'form-control', 'initial':''}),
            'cuenta_2': forms.TextInput(attrs={'class':'form-control'}),
            'moneda_2': forms.Select(choices=MONEDA_LIST, attrs={'class':'form-control', 'initial':''}),
            'clabe_2': forms.TextInput(attrs={'class':'form-control'}),
            'usar_en_portal_proveedores': forms.CheckboxInput(attrs={'class':'form-checkbox'}),
            'no_aplica_para_rafaga': forms.CheckboxInput(attrs={'class':'form-checkbox'}),
            'no_relacionar_OC': forms.CheckboxInput(attrs={'class':'form-checkbox'}),
            'constancia_situacion_fiscal': forms.FileInput(attrs={'class':'form-file'}),
            'estado_cuenta_bancario': forms.FileInput(attrs={'class':'form-file'}),
        }

class ProveedorDetailForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['empresa', 'codigo', 'tipo_alta', 'contribuyente', 'razon_social', 'rfc', 'curp', 'regimen_capital', 'nombre_fiscal', 'nombre_comercial', 'regimen_fiscal', 'uso_cdfi', 'representante_legal', 'telefono_1', 'telefono_2', 'contacto', 'grupo', 'correo_general', 'correo_pagos', 'sitio_web', 'rubro', 'tipo_operacion', 'tipo_tercero', 'id_fiscal', 'agente_aduanal', 'reg_inc_fiscal', 'impuesto_cedular', 'venc_s_fecha', 'dias_para_entrega_completa', 'limite_credito_MN', 'limite_credito_ME', 'dias_credito', 'monto_credito', 'retencion_iva', 'retencion_isr', 'iva_frontera', 'codigo_postal', 'pais', 'estado', 'ciudad', 'municipio', 'localidad', 'colonia', 'calle', 'numero_exterior', 'numero_interior', 'banco', 'cuenta', 'moneda', 'clabe', 'banco_2', 'cuenta_2', 'moneda_2', 'clabe_2', 'usar_en_portal_proveedores', 'no_aplica_para_rafaga', 'no_relacionar_OC']
        widgets = {
            'empresa': forms.Select(choices=EMPRESA_LIST, attrs={'class':'form-control', 'initial':''}),
            'codigo': forms.TextInput(attrs={'class':'form-control'}),
            'tipo_alta': forms.Select(choices=TIPO_ALTA_LIST, attrs={'class':'form-control', 'initial':''}),
            'contribuyente': forms.Select(choices=CONTRIBUYENTE_LIST, attrs={'class':'form-control', 'initial':''}),
            'razon_social': forms.TextInput(attrs={'class':'form-control'}),
            'rfc': forms.TextInput(attrs={'class':'form-control'}),
            'curp': forms.TextInput(attrs={'class':'form-control'}),
            'regimen_capital': forms.Select(choices=REGIMEN_CAPITAL_LIST, attrs={'class':'form-control', 'initial':''}),
            'nombre_fiscal': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_comercial': forms.TextInput(attrs={'class':'form-control'}),
            'regimen_fiscal': forms.Select(choices=REGIMEN_FISCAL_LIST, attrs={'class':'form-control', 'initial':''}),
            'uso_cdfi': forms.Select(choices=USO_CFDI_LIST, attrs={'class':'form-control', 'initial':''}),
            'representante_legal': forms.TextInput(attrs={'class':'form-control'}),
            'telefono_1': forms.TextInput(attrs={'class':'form-control'}),
            'telefono_2': forms.TextInput(attrs={'class':'form-control'}),
            'contacto': forms.TextInput(attrs={'class':'form-control'}),
            'grupo': forms.TextInput(attrs={'class':'form-control'}),
            'correo_general': forms.TextInput(attrs={'class':'form-control'}),
            'correo_pagos': forms.TextInput(attrs={'class':'form-control'}),
            'sitio_web': forms.TextInput(attrs={'class':'form-control'}),
            'rubro': forms.Select(choices=RUBRO_LIST, attrs={'class':'form-control', 'initial':''}),
            'tipo_operacion': forms.Select(choices=TIPO_OPERACION_LIST, attrs={'class':'form-control', 'initial':''}),
            'tipo_tercero': forms.Select(choices=TIPO_TERCERO_LIST, attrs={'class':'form-control', 'initial':''}),
            'id_fiscal': forms.TextInput(attrs={'class':'form-control'}),
            'agente_aduanal': forms.TextInput(attrs={'class':'form-control'}),
            'reg_inc_fiscal': forms.TextInput(attrs={'class':'form-control'}),
            'impuesto_cedular': forms.TextInput(attrs={'class':'form-control'}),
            'venc_s_fecha': forms.DateInput(attrs={'type':'date'}),
            'dias_para_entrega_completa': forms.TextInput(attrs={'class':'form-control'}),
            'limite_credito_MN': forms.TextInput(attrs={'class':'form-control'}),
            'limite_credito_ME': forms.TextInput(attrs={'class':'form-control'}),
            'dias_credito': forms.TextInput(attrs={'class':'form-control'}),
            'monto_credito': forms.TextInput(attrs={'class':'form-control'}),
            'retencion_iva': forms.Select(choices=RETENCION_IVA_LIST, attrs={'class':'form-control', 'initial':''}),
            'retencion_isr': forms.Select(choices=RETENCION_ISR_LIST, attrs={'class':'form-control', 'initial':''}),
            'iva_frontera': forms.Select(choices=IVA_FRONTERA_LIST, attrs={'class':'form-control', 'initial':''}),
            'codigo_postal': forms.TextInput(attrs={'class':'form-control'}),
            'pais': forms.TextInput(attrs={'class':'form-control'}),
            'estado': forms.TextInput(attrs={'class':'form-control'}),
            'ciudad': forms.TextInput(attrs={'class':'form-control'}),
            'municipio': forms.TextInput(attrs={'class':'form-control'}),
            'localidad': forms.TextInput(attrs={'class':'form-control'}),
            'colonia': forms.TextInput(attrs={'class':'form-control'}),
            'calle': forms.TextInput(attrs={'class':'form-control'}),
            'numero_exterior': forms.TextInput(attrs={'class':'form-control'}),
            'numero_interior': forms.TextInput(attrs={'class':'form-control'}),
            'banco': forms.Select(choices=BANCO_LIST, attrs={'class':'form-control', 'initial':''}),
            'cuenta': forms.TextInput(attrs={'class':'form-control'}),
            'moneda': forms.Select(choices=MONEDA_LIST, attrs={'class':'form-control', 'initial':''}),
            'clabe': forms.TextInput(attrs={'class':'form-control'}),
            'banco_2': forms.Select(choices=BANCO_LIST, attrs={'class':'form-control', 'initial':''}),
            'cuenta_2': forms.TextInput(attrs={'class':'form-control'}),
            'moneda_2': forms.Select(choices=MONEDA_LIST, attrs={'class':'form-control', 'initial':''}),
            'clabe_2': forms.TextInput(attrs={'class':'form-control'}),
            'usar_en_portal_proveedores': forms.CheckboxInput(attrs={'class':'form-checkbox'}),
            'no_aplica_para_rafaga': forms.CheckboxInput(attrs={'class':'form-checkbox'}),
            'no_relacionar_OC': forms.CheckboxInput(attrs={'class':'form-checkbox'}),
        }

class ProveedorFormForCompras(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['empresa', 'codigo', 'tipo_alta', 'contribuyente', 'razon_social', 'rfc', 'curp', 'regimen_capital', 'nombre_fiscal', 'nombre_comercial', 'regimen_fiscal', 'uso_cdfi', 'representante_legal', 'telefono_1', 'telefono_2', 'contacto', 'grupo', 'correo_general', 'correo_pagos', 'sitio_web', 'rubro', 'tipo_operacion', 'tipo_tercero', 'id_fiscal', 'agente_aduanal', 'reg_inc_fiscal', 'impuesto_cedular', 'venc_s_fecha', 'dias_para_entrega_completa', 'limite_credito_MN', 'limite_credito_ME', 'dias_credito', 'monto_credito', 'retencion_iva', 'retencion_isr', 'iva_frontera', 'codigo_postal', 'pais', 'estado', 'ciudad', 'municipio', 'localidad', 'colonia', 'calle', 'numero_exterior', 'numero_interior', 'banco', 'cuenta', 'moneda', 'clabe', 'banco_2', 'cuenta_2', 'moneda_2', 'clabe_2', 'usar_en_portal_proveedores', 'no_aplica_para_rafaga', 'no_relacionar_OC', 'compras']
        widgets = {
            'empresa': forms.Select(choices=EMPRESA_LIST, attrs={'class':'form-control', 'initial':''}),
            'codigo': forms.TextInput(attrs={'class':'form-control'}),
            'tipo_alta': forms.Select(choices=TIPO_ALTA_LIST, attrs={'class':'form-control', 'initial':''}),
            'contribuyente': forms.Select(choices=CONTRIBUYENTE_LIST, attrs={'class':'form-control', 'initial':''}),
            'razon_social': forms.TextInput(attrs={'class':'form-control'}),
            'rfc': forms.TextInput(attrs={'class':'form-control'}),
            'curp': forms.TextInput(attrs={'class':'form-control'}),
            'regimen_capital': forms.Select(choices=REGIMEN_CAPITAL_LIST, attrs={'class':'form-control', 'initial':''}),
            'nombre_fiscal': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_comercial': forms.TextInput(attrs={'class':'form-control'}),
            'regimen_fiscal': forms.Select(choices=REGIMEN_FISCAL_LIST, attrs={'class':'form-control', 'initial':''}),
            'uso_cdfi': forms.Select(choices=USO_CFDI_LIST, attrs={'class':'form-control', 'initial':''}),
            'representante_legal': forms.TextInput(attrs={'class':'form-control'}),
            'telefono_1': forms.TextInput(attrs={'class':'form-control'}),
            'telefono_2': forms.TextInput(attrs={'class':'form-control'}),
            'contacto': forms.TextInput(attrs={'class':'form-control'}),
            'grupo': forms.TextInput(attrs={'class':'form-control'}),
            'correo_general': forms.TextInput(attrs={'class':'form-control'}),
            'correo_pagos': forms.TextInput(attrs={'class':'form-control'}),
            'sitio_web': forms.TextInput(attrs={'class':'form-control'}),
            'rubro': forms.Select(choices=RUBRO_LIST, attrs={'class':'form-control', 'initial':''}),
            'tipo_operacion': forms.Select(choices=TIPO_OPERACION_LIST, attrs={'class':'form-control', 'initial':''}),
            'tipo_tercero': forms.Select(choices=TIPO_TERCERO_LIST, attrs={'class':'form-control', 'initial':''}),
            'id_fiscal': forms.TextInput(attrs={'class':'form-control'}),
            'agente_aduanal': forms.TextInput(attrs={'class':'form-control'}),
            'reg_inc_fiscal': forms.TextInput(attrs={'class':'form-control'}),
            'impuesto_cedular': forms.TextInput(attrs={'class':'form-control'}),
            'venc_s_fecha': forms.DateInput(attrs={'type':'date'}),
            'dias_para_entrega_completa': forms.TextInput(attrs={'class':'form-control'}),
            'limite_credito_MN': forms.TextInput(attrs={'class':'form-control'}),
            'limite_credito_ME': forms.TextInput(attrs={'class':'form-control'}),
            'dias_credito': forms.TextInput(attrs={'class':'form-control'}),
            'monto_credito': forms.TextInput(attrs={'class':'form-control'}),
            'retencion_iva': forms.Select(choices=RETENCION_IVA_LIST, attrs={'class':'form-control', 'initial':''}),
            'retencion_isr': forms.Select(choices=RETENCION_ISR_LIST, attrs={'class':'form-control', 'initial':''}),
            'iva_frontera': forms.Select(choices=IVA_FRONTERA_LIST, attrs={'class':'form-control', 'initial':''}),
            'codigo_postal': forms.TextInput(attrs={'class':'form-control'}),
            'pais': forms.TextInput(attrs={'class':'form-control'}),
            'estado': forms.TextInput(attrs={'class':'form-control'}),
            'ciudad': forms.TextInput(attrs={'class':'form-control'}),
            'municipio': forms.TextInput(attrs={'class':'form-control'}),
            'localidad': forms.TextInput(attrs={'class':'form-control'}),
            'colonia': forms.TextInput(attrs={'class':'form-control'}),
            'calle': forms.TextInput(attrs={'class':'form-control'}),
            'numero_exterior': forms.TextInput(attrs={'class':'form-control'}),
            'numero_interior': forms.TextInput(attrs={'class':'form-control'}),
            'banco': forms.Select(choices=BANCO_LIST, attrs={'class':'form-control', 'initial':''}),
            'cuenta': forms.TextInput(attrs={'class':'form-control'}),
            'moneda': forms.Select(choices=MONEDA_LIST, attrs={'class':'form-control', 'initial':''}),
            'clabe': forms.TextInput(attrs={'class':'form-control'}),
            'banco_2': forms.Select(choices=BANCO_LIST, attrs={'class':'form-control', 'initial':''}),
            'cuenta_2': forms.TextInput(attrs={'class':'form-control'}),
            'moneda_2': forms.Select(choices=MONEDA_LIST, attrs={'class':'form-control', 'initial':''}),
            'clabe_2': forms.TextInput(attrs={'class':'form-control'}),
            'usar_en_portal_proveedores': forms.CheckboxInput(attrs={'class':'form-checkbox'}),
            'no_aplica_para_rafaga': forms.CheckboxInput(attrs={'class':'form-checkbox'}),
            'no_relacionar_OC': forms.CheckboxInput(attrs={'class':'form-checkbox'}),
            'compras': forms.CheckboxInput(attrs={'class':'form-checkbox'}),
        }

class ProveedorFormForFinanzas(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['empresa', 'codigo', 'tipo_alta', 'contribuyente', 'razon_social', 'rfc', 'curp', 'regimen_capital', 'nombre_fiscal', 'nombre_comercial', 'regimen_fiscal', 'uso_cdfi', 'representante_legal', 'telefono_1', 'telefono_2', 'contacto', 'grupo', 'correo_general', 'correo_pagos', 'sitio_web', 'rubro', 'tipo_operacion', 'tipo_tercero', 'id_fiscal', 'agente_aduanal', 'reg_inc_fiscal', 'impuesto_cedular', 'venc_s_fecha', 'dias_para_entrega_completa', 'limite_credito_MN', 'limite_credito_ME', 'dias_credito', 'monto_credito', 'retencion_iva', 'retencion_isr', 'iva_frontera', 'codigo_postal', 'pais', 'estado', 'ciudad', 'municipio', 'localidad', 'colonia', 'calle', 'numero_exterior', 'numero_interior', 'banco', 'cuenta', 'moneda', 'clabe', 'banco_2', 'cuenta_2', 'moneda_2', 'clabe_2', 'usar_en_portal_proveedores', 'no_aplica_para_rafaga', 'no_relacionar_OC', 'finanzas']
        widgets = {
            'empresa': forms.Select(choices=EMPRESA_LIST, attrs={'class':'form-control', 'initial':''}),
            'codigo': forms.TextInput(attrs={'class':'form-control'}),
            'tipo_alta': forms.Select(choices=TIPO_ALTA_LIST, attrs={'class':'form-control', 'initial':''}),
            'contribuyente': forms.Select(choices=CONTRIBUYENTE_LIST, attrs={'class':'form-control', 'initial':''}),
            'razon_social': forms.TextInput(attrs={'class':'form-control'}),
            'rfc': forms.TextInput(attrs={'class':'form-control'}),
            'curp': forms.TextInput(attrs={'class':'form-control'}),
            'regimen_capital': forms.Select(choices=REGIMEN_CAPITAL_LIST, attrs={'class':'form-control', 'initial':''}),
            'nombre_fiscal': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_comercial': forms.TextInput(attrs={'class':'form-control'}),
            'regimen_fiscal': forms.Select(choices=REGIMEN_FISCAL_LIST, attrs={'class':'form-control', 'initial':''}),
            'uso_cdfi': forms.Select(choices=USO_CFDI_LIST, attrs={'class':'form-control', 'initial':''}),
            'representante_legal': forms.TextInput(attrs={'class':'form-control'}),
            'telefono_1': forms.TextInput(attrs={'class':'form-control'}),
            'telefono_2': forms.TextInput(attrs={'class':'form-control'}),
            'contacto': forms.TextInput(attrs={'class':'form-control'}),
            'grupo': forms.TextInput(attrs={'class':'form-control'}),
            'correo_general': forms.TextInput(attrs={'class':'form-control'}),
            'correo_pagos': forms.TextInput(attrs={'class':'form-control'}),
            'sitio_web': forms.TextInput(attrs={'class':'form-control'}),
            'rubro': forms.Select(choices=RUBRO_LIST, attrs={'class':'form-control', 'initial':''}),
            'tipo_operacion': forms.Select(choices=TIPO_OPERACION_LIST, attrs={'class':'form-control', 'initial':''}),
            'tipo_tercero': forms.Select(choices=TIPO_TERCERO_LIST, attrs={'class':'form-control', 'initial':''}),
            'id_fiscal': forms.TextInput(attrs={'class':'form-control'}),
            'agente_aduanal': forms.TextInput(attrs={'class':'form-control'}),
            'reg_inc_fiscal': forms.TextInput(attrs={'class':'form-control'}),
            'impuesto_cedular': forms.TextInput(attrs={'class':'form-control'}),
            'venc_s_fecha': forms.DateInput(attrs={'type':'date'}),
            'dias_para_entrega_completa': forms.TextInput(attrs={'class':'form-control'}),
            'limite_credito_MN': forms.TextInput(attrs={'class':'form-control'}),
            'limite_credito_ME': forms.TextInput(attrs={'class':'form-control'}),
            'dias_credito': forms.TextInput(attrs={'class':'form-control'}),
            'monto_credito': forms.TextInput(attrs={'class':'form-control'}),
            'retencion_iva': forms.Select(choices=RETENCION_IVA_LIST, attrs={'class':'form-control', 'initial':''}),
            'retencion_isr': forms.Select(choices=RETENCION_ISR_LIST, attrs={'class':'form-control', 'initial':''}),
            'iva_frontera': forms.Select(choices=IVA_FRONTERA_LIST, attrs={'class':'form-control', 'initial':''}),
            'codigo_postal': forms.TextInput(attrs={'class':'form-control'}),
            'pais': forms.TextInput(attrs={'class':'form-control'}),
            'estado': forms.TextInput(attrs={'class':'form-control'}),
            'ciudad': forms.TextInput(attrs={'class':'form-control'}),
            'municipio': forms.TextInput(attrs={'class':'form-control'}),
            'localidad': forms.TextInput(attrs={'class':'form-control'}),
            'colonia': forms.TextInput(attrs={'class':'form-control'}),
            'calle': forms.TextInput(attrs={'class':'form-control'}),
            'numero_exterior': forms.TextInput(attrs={'class':'form-control'}),
            'numero_interior': forms.TextInput(attrs={'class':'form-control'}),
            'banco': forms.Select(choices=BANCO_LIST, attrs={'class':'form-control', 'initial':''}),
            'cuenta': forms.TextInput(attrs={'class':'form-control'}),
            'moneda': forms.Select(choices=MONEDA_LIST, attrs={'class':'form-control', 'initial':''}),
            'clabe': forms.TextInput(attrs={'class':'form-control'}),
            'banco_2': forms.Select(choices=BANCO_LIST, attrs={'class':'form-control', 'initial':''}),
            'cuenta_2': forms.TextInput(attrs={'class':'form-control'}),
            'moneda_2': forms.Select(choices=MONEDA_LIST, attrs={'class':'form-control', 'initial':''}),
            'clabe_2': forms.TextInput(attrs={'class':'form-control'}),
            'usar_en_portal_proveedores': forms.CheckboxInput(attrs={'class':'form-checkbox'}),
            'no_aplica_para_rafaga': forms.CheckboxInput(attrs={'class':'form-checkbox'}),
            'no_relacionar_OC': forms.CheckboxInput(attrs={'class':'form-checkbox'}),
            'finanzas': forms.CheckboxInput(attrs={'class':'form-checkbox'}),
        }

class ProveedorFormForSistemas(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['empresa', 'codigo', 'tipo_alta', 'contribuyente', 'razon_social', 'rfc', 'curp', 'regimen_capital', 'nombre_fiscal', 'nombre_comercial', 'regimen_fiscal', 'uso_cdfi', 'representante_legal', 'telefono_1', 'telefono_2', 'contacto', 'grupo', 'correo_general', 'correo_pagos', 'sitio_web', 'rubro', 'tipo_operacion', 'tipo_tercero', 'id_fiscal', 'agente_aduanal', 'reg_inc_fiscal', 'impuesto_cedular', 'venc_s_fecha', 'dias_para_entrega_completa', 'limite_credito_MN', 'limite_credito_ME', 'dias_credito', 'monto_credito', 'retencion_iva', 'retencion_isr', 'iva_frontera', 'codigo_postal', 'pais', 'estado', 'ciudad', 'municipio', 'localidad', 'colonia', 'calle', 'numero_exterior', 'numero_interior', 'banco', 'cuenta', 'moneda', 'clabe', 'banco_2', 'cuenta_2', 'moneda_2', 'clabe_2', 'usar_en_portal_proveedores', 'no_aplica_para_rafaga', 'no_relacionar_OC', 'sistemas']
        widgets = {
            'empresa': forms.Select(choices=EMPRESA_LIST, attrs={'class':'form-control', 'initial':''}),
            'codigo': forms.TextInput(attrs={'class':'form-control'}),
            'tipo_alta': forms.Select(choices=TIPO_ALTA_LIST, attrs={'class':'form-control', 'initial':''}),
            'contribuyente': forms.Select(choices=CONTRIBUYENTE_LIST, attrs={'class':'form-control', 'initial':''}),
            'razon_social': forms.TextInput(attrs={'class':'form-control'}),
            'rfc': forms.TextInput(attrs={'class':'form-control'}),
            'curp': forms.TextInput(attrs={'class':'form-control'}),
            'regimen_capital': forms.Select(choices=REGIMEN_CAPITAL_LIST, attrs={'class':'form-control', 'initial':''}),
            'nombre_fiscal': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_comercial': forms.TextInput(attrs={'class':'form-control'}),
            'regimen_fiscal': forms.Select(choices=REGIMEN_FISCAL_LIST, attrs={'class':'form-control', 'initial':''}),
            'uso_cdfi': forms.Select(choices=USO_CFDI_LIST, attrs={'class':'form-control', 'initial':''}),
            'representante_legal': forms.TextInput(attrs={'class':'form-control'}),
            'telefono_1': forms.TextInput(attrs={'class':'form-control'}),
            'telefono_2': forms.TextInput(attrs={'class':'form-control'}),
            'contacto': forms.TextInput(attrs={'class':'form-control'}),
            'grupo': forms.TextInput(attrs={'class':'form-control'}),
            'correo_general': forms.TextInput(attrs={'class':'form-control'}),
            'correo_pagos': forms.TextInput(attrs={'class':'form-control'}),
            'sitio_web': forms.TextInput(attrs={'class':'form-control'}),
            'rubro': forms.Select(choices=RUBRO_LIST, attrs={'class':'form-control', 'initial':''}),
            'tipo_operacion': forms.Select(choices=TIPO_OPERACION_LIST, attrs={'class':'form-control', 'initial':''}),
            'tipo_tercero': forms.Select(choices=TIPO_TERCERO_LIST, attrs={'class':'form-control', 'initial':''}),
            'id_fiscal': forms.TextInput(attrs={'class':'form-control'}),
            'agente_aduanal': forms.TextInput(attrs={'class':'form-control'}),
            'reg_inc_fiscal': forms.TextInput(attrs={'class':'form-control'}),
            'impuesto_cedular': forms.TextInput(attrs={'class':'form-control'}),
            'venc_s_fecha': forms.DateInput(attrs={'type':'date'}),
            'dias_para_entrega_completa': forms.TextInput(attrs={'class':'form-control'}),
            'limite_credito_MN': forms.TextInput(attrs={'class':'form-control'}),
            'limite_credito_ME': forms.TextInput(attrs={'class':'form-control'}),
            'dias_credito': forms.TextInput(attrs={'class':'form-control'}),
            'monto_credito': forms.TextInput(attrs={'class':'form-control'}),
            'retencion_iva': forms.Select(choices=RETENCION_IVA_LIST, attrs={'class':'form-control', 'initial':''}),
            'retencion_isr': forms.Select(choices=RETENCION_ISR_LIST, attrs={'class':'form-control', 'initial':''}),
            'iva_frontera': forms.Select(choices=IVA_FRONTERA_LIST, attrs={'class':'form-control', 'initial':''}),
            'codigo_postal': forms.TextInput(attrs={'class':'form-control'}),
            'pais': forms.TextInput(attrs={'class':'form-control'}),
            'estado': forms.TextInput(attrs={'class':'form-control'}),
            'ciudad': forms.TextInput(attrs={'class':'form-control'}),
            'municipio': forms.TextInput(attrs={'class':'form-control'}),
            'localidad': forms.TextInput(attrs={'class':'form-control'}),
            'colonia': forms.TextInput(attrs={'class':'form-control'}),
            'calle': forms.TextInput(attrs={'class':'form-control'}),
            'numero_exterior': forms.TextInput(attrs={'class':'form-control'}),
            'numero_interior': forms.TextInput(attrs={'class':'form-control'}),
            'banco': forms.Select(choices=BANCO_LIST, attrs={'class':'form-control', 'initial':''}),
            'cuenta': forms.TextInput(attrs={'class':'form-control'}),
            'moneda': forms.Select(choices=MONEDA_LIST, attrs={'class':'form-control', 'initial':''}),
            'clabe': forms.TextInput(attrs={'class':'form-control'}),
            'banco_2': forms.Select(choices=BANCO_LIST, attrs={'class':'form-control', 'initial':''}),
            'cuenta_2': forms.TextInput(attrs={'class':'form-control'}),
            'moneda_2': forms.Select(choices=MONEDA_LIST, attrs={'class':'form-control', 'initial':''}),
            'clabe_2': forms.TextInput(attrs={'class':'form-control'}),
            'usar_en_portal_proveedores': forms.CheckboxInput(attrs={'class':'form-checkbox'}),
            'no_aplica_para_rafaga': forms.CheckboxInput(attrs={'class':'form-checkbox'}),
            'no_relacionar_OC': forms.CheckboxInput(attrs={'class':'form-checkbox'}),
            'sistemas': forms.CheckboxInput(attrs={'class':'form-checkbox'}),
        }