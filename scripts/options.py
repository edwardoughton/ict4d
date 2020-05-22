"""
Options consisting of scenarios and strategies.

Country parameters consist of those parameters which are specific
to each country.

Written by Ed Oughton

January 2020

#strategy is defined based on generation_core_backhaul_sharing_networks_spectrum_tax_integration

generation: technology generation, so 3G or 4G
core: type of core data transport network, eg. evolved packet core (4G)
backhaul: type of backhaul, so fiber or microwave
sharing: the type of infrastructure sharing, active, passive etc..
network: relates to the number of networks, as defined in country parameters
spectrum: type of spectrum strategy, so baseline, high or low
tax: type of taxation strategy, so baseline, high or low
integration: option to undertake regional integration

"""

OPTIONS = {
    'technology_options': [
        {
            'scenario': 'S1_2_2_2',
            'strategy': '3G_epc_microwave_baseline_baseline_baseline_baseline_baseline',
        },
        {
            'scenario': 'S1_2_2_2',
            'strategy': '3G_epc_fiber_baseline_baseline_baseline_baseline_baseline',
        },
        {
            'scenario': 'S1_2_2_2',
            'strategy': '4G_epc_microwave_baseline_baseline_baseline_baseline_baseline',
        },
        {
            'scenario': 'S1_2_2_2',
            'strategy': '4G_epc_fiber_baseline_baseline_baseline_baseline_baseline',
        },
    ],
    'business_model_options': [
        {
            'scenario': 'S1_2_2_2',
            'strategy': '4G_epc_microwave_baseline_baseline_baseline_baseline_baseline',
        },
        {
            'scenario': 'S1_2_2_2',
            'strategy': '4G_epc_microwave_pss_baseline_baseline_baseline_baseline',
        },
        {
            'scenario': 'S1_2_2_2',
            'strategy': '4G_epc_microwave_psb_baseline_baseline_baseline_baseline',
        },
        {
            'scenario': 'S1_2_2_2',
            'strategy': '4G_epc_microwave_moran_baseline_baseline_baseline_baseline',
        },
        ### {
        ###     'scenario': 'S1_2_2_2',
        ###     'strategy': '4G_epc_microwave_mocn_baseline_baseline_baseline_baseline',
        ### },
        {
            'scenario': 'S1_2_2_2',
            'strategy': '4G_epc_microwave_cns_baseline_baseline_baseline_baseline',
        },
        {
            'scenario': 'S1_2_2_2', #single shared core network
            'strategy': '4G_epc_microwave_baseline_srn_baseline_baseline_baseline',
        },
    ],
    'integration_options': [
        {
            'scenario': 'S1_2_2_2',
            'strategy': '3G_epc_microwave_baseline_baseline_baseline_baseline_integration',
        },
        {
            'scenario': 'S1_2_2_2',
            'strategy': '3G_epc_fiber_baseline_baseline_baseline_baseline_integration',
        },
        {
            'scenario': 'S1_2_2_2',
            'strategy': '4G_epc_microwave_baseline_baseline_baseline_baseline_integration',
        },
        {
            'scenario': 'S1_2_2_2',
            'strategy': '4G_epc_fiber_baseline_baseline_baseline_baseline_integration',
        },
    ]
}


COUNTRY_PARAMETERS = {
    'CIV': {
        'luminosity': {
            'high': 5,
            'medium': 1,
        },
        'arpu': {
            'high': 10,
            'medium': 7,
            'low': 5,
        },
        'networks': {
            'baseline_urban': 3,
            'baseline_suburban': 3,
            'baseline_rural': 3,
        },
        'frequencies': {
            '3G': [
                {
                    'frequency': 1800,
                    'bandwidth': '2x10',
                },
                {
                    'frequency': 2100,
                    'bandwidth': '2x10',
                },
            ],
            '4G': [
                {
                    'frequency': 800,
                    'bandwidth': '2x10',
                },
                {
                    'frequency': 1800,
                    'bandwidth': '2x10',
                },
            ],
        },
        'financials': {
            'wacc': 15,
            'profit_margin': 10,
            'spectrum_coverage_baseline_usd_mhz_pop': 0.025,
            'spectrum_capacity_baseline_usd_mhz_pop': 0.02,
            'tax_low': 10,
            'tax_baseline': 25,
            'tax_high': 40,
            'ops_and_acquisition_per_subscriber': 2,
            },
        },
    'MLI': {
        'luminosity': {
            'high': 5,
            'medium': 1,
        },
        'arpu': {
            'high': 15,
            'medium': 10,
            'low': 5,
        },
        'networks': {
            'baseline_urban': 3,
            'baseline_suburban': 3,
            'baseline_rural': 3,
        },
        'frequencies': {
            '3G': [
                {
                    'frequency': 1800,
                    'bandwidth': '2x10',
                },
                {
                    'frequency': 2100,
                    'bandwidth': '2x10',
                },
            ],
            '4G': [
                {
                    'frequency': 800,
                    'bandwidth': '2x10',
                },
                {
                    'frequency': 1800,
                    'bandwidth': '2x10',
                },
            ],
        },
        'financials': {
            'wacc': 15,
            'profit_margin': 10,
            'spectrum_coverage_baseline_usd_mhz_pop': 0.025,
            'spectrum_capacity_baseline_usd_mhz_pop': 0.02,
            'tax_low': 10,
            'tax_baseline': 25,
            'tax_high': 40,
            'ops_and_acquisition_per_subscriber': 2,
            },
        },
    'SEN': {
        'luminosity': {
            'high': 5,
            'medium': 1,
        },
        'arpu': {
            'high': 10,
            'medium': 8,
            'low': 5,
        },
        'networks': {
            'baseline_urban': 3,
            'baseline_suburban': 3,
            'baseline_rural': 3,
        },
        'frequencies': {
            '3G': [
                {
                    'frequency': 1800,
                    'bandwidth': '2x10',
                },
                {
                    'frequency': 2100,
                    'bandwidth': '2x10',
                },
            ],
            '4G': [
                {
                    'frequency': 800,
                    'bandwidth': '2x10',
                },
                {
                    'frequency': 1800,
                    'bandwidth': '2x10',
                },
            ],
        },
        'financials': {
            'wacc': 15,
            'profit_margin': 10,
            'spectrum_coverage_baseline_usd_mhz_pop': 0.1,
            'spectrum_capacity_baseline_usd_mhz_pop': 0.08,
            'spectrum_cost_low': 50,
            'spectrum_cost_high': 50,
            'tax_low': 10,
            'tax_baseline': 30,
            'tax_high': 40,
            'ops_and_acquisition_per_subscriber': 4,
            },
        },


    'KEN': {
        'luminosity': {
            'high': 5,
            'medium': 1,
        },
        'arpu': {
            'high': 12,
            'medium': 9,
            'low': 5,
        },
        'networks': {
            'baseline_urban': 3,
            'baseline_suburban': 3,
            'baseline_rural': 3,
        },
        'frequencies': {
            '3G': [
                {
                    'frequency': 1800,
                    'bandwidth': '2x10',
                },
                {
                    'frequency': 2100,
                    'bandwidth': '2x10',
                },
            ],
            '4G': [
                {
                    'frequency': 800,
                    'bandwidth': '2x10',
                },
                {
                    'frequency': 1800,
                    'bandwidth': '2x10',
                },
            ],
        },
        'financials': {
            'wacc': 15,
            'profit_margin': 10,
            'spectrum_coverage_baseline_usd_mhz_pop': 0.1,
            'spectrum_capacity_baseline_usd_mhz_pop': 0.08,
            'tax_low': 10,
            'tax_baseline': 25,
            'tax_high': 40,
            'ops_and_acquisition_per_subscriber': 2,
            },
        },
        'TZA': {
        'luminosity': {
            'high': 5,
            'medium': 1,
        },
        'arpu': {
            'high': 10,
            'medium': 3,
            'low': 2,
        },
        'networks': {
            'baseline_urban': 3,
            'baseline_suburban': 3,
            'baseline_rural': 3,
        },
        'frequencies': {
            '3G': [
                {
                    'frequency': 1800,
                    'bandwidth': '2x10',
                },
                {
                    'frequency': 2100,
                    'bandwidth': '2x10',
                },
            ],
            '4G': [
                {
                    'frequency': 800,
                    'bandwidth': '2x10',
                },
                {
                    'frequency': 1800,
                    'bandwidth': '2x10',
                },
            ],
        },
        'financials': {
            'wacc': 15,
            'profit_margin': 10,
            'subsidy_low': 10,
            'subsidy_high': 40,
            'spectrum_coverage_baseline_usd_mhz_pop': 0.1,
            'spectrum_capacity_baseline_usd_mhz_pop': 0.08,
            'tax_low': 10,
            'tax_baseline': 25,
            'tax_high': 40,
            'ops_and_acquisition_per_subscriber': 2,
            },
        },
    'UGA': {
        'luminosity': {
            'high': 5,
            'medium': 1,
        },
        'arpu': {
            'high': 10,
            'medium': 3,
            'low': 2,
        },
        'networks': {
            'baseline_urban': 3,
            'baseline_suburban': 3,
            'baseline_rural': 3,
        },
        'frequencies': {
            '3G': [
                {
                    'frequency': 1800,
                    'bandwidth': '2x10',
                },
                {
                    'frequency': 2100,
                    'bandwidth': '2x10',
                },
            ],
            '4G': [
                {
                    'frequency': 800,
                    'bandwidth': '2x10',
                },
                {
                    'frequency': 1800,
                    'bandwidth': '2x10',
                },
            ],
        },
        'financials': {
            'wacc': 15,
            'profit_margin': 10,
            'subsidy_low': 10,
            'subsidy_high': 40,
            'spectrum_coverage_baseline_usd_mhz_pop': 0.025,
            'spectrum_capacity_baseline_usd_mhz_pop': 0.02,
            'tax_low': 10,
            'tax_baseline': 25,
            'tax_high': 40,
            'ops_and_acquisition_per_subscriber': 2,
            },
        },
    'SEN-MLI-CIV': {
        'luminosity': {
            'high': 5,
            'medium': 1,
        },
        'arpu': {
            'high': 10,
            'medium': 7,
            'low': 5,
        },
        'networks': {
            'baseline_urban': 3,
            'baseline_suburban': 3,
            'baseline_rural': 3,
        },
        'frequencies': {
            '3G': [
                {
                    'frequency': 1800,
                    'bandwidth': '2x10',
                },
                {
                    'frequency': 2100,
                    'bandwidth': '2x10',
                },
            ],
            '4G': [
                {
                    'frequency': 800,
                    'bandwidth': '2x10',
                },
                {
                    'frequency': 1800,
                    'bandwidth': '2x10',
                },
            ],
        },
        'financials': {
            'wacc': 15,
            'profit_margin': 10,
            'spectrum_coverage_baseline_usd_mhz_pop': 0.025,
            'spectrum_capacity_baseline_usd_mhz_pop': 0.02,
            'tax_low': 10,
            'tax_baseline': 25,
            'tax_high': 40,
            'ops_and_acquisition_per_subscriber': 2,
            },
        },
    'KEN-TZA-UGA': {
        'luminosity': {
            'high': 5,
            'medium': 1,
        },
        'arpu': {
            'high': 10,
            'medium': 7,
            'low': 5,
        },
        'networks': {
            'baseline_urban': 3,
            'baseline_suburban': 3,
            'baseline_rural': 3,
        },
        'frequencies': {
            '3G': [
                {
                    'frequency': 1800,
                    'bandwidth': '2x10',
                },
                {
                    'frequency': 2100,
                    'bandwidth': '2x10',
                },
            ],
            '4G': [
                {
                    'frequency': 800,
                    'bandwidth': '2x10',
                },
                {
                    'frequency': 1800,
                    'bandwidth': '2x10',
                },
            ],
        },
        'financials': {
            'wacc': 15,
            'profit_margin': 10,
            'spectrum_coverage_baseline_usd_mhz_pop': 0.025,
            'spectrum_capacity_baseline_usd_mhz_pop': 0.02,
            'tax_low': 10,
            'tax_baseline': 25,
            'tax_high': 40,
            'ops_and_acquisition_per_subscriber': 2,
            },
        },
    }
